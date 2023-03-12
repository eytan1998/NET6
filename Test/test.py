from Backend.Help.app_packet import AppHeader
from Backend.RUDP.CC import CC, START_CWND, SLOW_START, AIMD, MAX_SIZE
from Backend.RUDP.rudp_packet import RUDP_Header
import unittest


class ChecksumTest(unittest.TestCase):
    def test_checksum(self):
        send = RUDP_Header(1, 2, None, 0, False, True, False, False, 1234
                           , b'asd')
        send.checksum = RUDP_Header.checksum_func(send.pack())
        send = send.pack()
        print(send)
        # after no change return true

        self.assertTrue(RUDP_Header.verify_checksum(RUDP_Header.unpack(send)))
        # change send
        send = send.replace(b'\x04', b"\xff", 1)
        print(send)

        # after change return false
        self.assertFalse(RUDP_Header.verify_checksum(RUDP_Header.unpack(send)))


class CCTest(unittest.TestCase):
    def test_win_raise(self):
        newCC = CC()
        self.assertEqual(newCC.getCWND(), START_CWND)
        newCC.raiseCWND()
        self.assertEqual(newCC.getCWND(), START_CWND * 2)
        newCC.raiseCWND()
        self.assertEqual(newCC.getCWND(), START_CWND * 4)

    def test_win_low(self):
        newCC = CC()
        newCC.raiseCWND()
        newCC.raiseCWND()
        newCC.raiseCWND()  # START_CWND * 8
        newCC.lowCWND()  # back to Start
        self.assertEqual(newCC.getCWND(), START_CWND)

    def test_win_ssthresh(self):
        newCC = CC()
        newCC.raiseCWND()
        newCC.raiseCWND()
        newCC.raiseCWND()  # START_CWND * 8
        newCC.lowCWND()  # back to Start,ssthresh (half of cwnd)= START_CWND * 8/2 = START_CWND * 4
        self.assertEqual(newCC.ssthresh, START_CWND * 4)

    def test_win_state(self):
        newCC = CC()
        newCC.raiseCWND()
        newCC.raiseCWND()
        newCC.raiseCWND()  # START_CWND * 8
        newCC.lowCWND()  # back to Start,ssthresh (half of cwnd)= START_CWND * 8/2 = START_CWND * 4
        self.assertEqual(newCC.ssthresh, START_CWND * 4)
        newCC.raiseCWND()
        self.assertEqual(newCC.STATE, SLOW_START)
        newCC.raiseCWND()  # got to ssthresh became aimd state
        self.assertEqual(newCC.STATE, AIMD)
        newCC.raiseCWND()  # incr by one
        # START_CWND * 4 + 1
        self.assertEqual(newCC.cwnd, START_CWND * 4 + 1)

    def test_win_max(self):
        newCC = CC()
        for i in range(100):
            newCC.raiseCWND()
        self.assertEqual(newCC.cwnd, MAX_SIZE)


if __name__ == '__main__':
    test_checksum = ChecksumTest()
    test_checksum.test_checksum()

    test_checksum = CCTest()
    test_checksum.test_win_raise()
    test_checksum.test_win_low()
    test_checksum.test_win_ssthresh()
    test_checksum.test_win_state()
    test_checksum.test_win_max()


