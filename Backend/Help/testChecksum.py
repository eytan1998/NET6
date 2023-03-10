from RUDP.rudp_packet import RUDP_Header

if __name__ == '__main__':
    send = RUDP_Header(1, 2, None, 0, False, True, False, False, 1234
                       , b'asd')
    send.checksum = RUDP_Header.checksum_func(send.pack())
    send = send.pack()
    print(send)
    # after no change return true
    print(RUDP_Header.verify_checksum(RUDP_Header.unpack(send)))
    # change send
    send = send.replace(b'\x04',b"\xff", 1)
    print(send)

    # after change return false
    print(RUDP_Header.verify_checksum(RUDP_Header.unpack(send)))