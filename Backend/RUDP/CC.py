SLOW_START = "SLOW START"
AIMD = "AIMD"
START_CWND = 100
MAX_SIZE = 65535


class CC:

    def __init__(self):
        self.ssthresh = 9999999
        self.STATE = SLOW_START
        self.cwnd = START_CWND

    def raiseCWND(self):
        # slow start multi by 2
        if self.STATE == SLOW_START:
            self.cwnd *= 2
            if self.cwnd >= MAX_SIZE:
                self.cwnd = MAX_SIZE
            # change state if needed
            if self.cwnd >= self.ssthresh:
                self.STATE = AIMD
        # aimd incr by 1
        elif self.STATE == AIMD:
            self.cwnd += 1
        # print("raise CWND to :" + str(self.cwnd))

    def lowCWND(self):
        # thresh to half and start over with slow start
        self.ssthresh = int(self.cwnd / 2)
        self.cwnd = START_CWND
        self.STATE = SLOW_START
        # print("lower CWND to :" + str(self.cwnd))

    def getCWND(self):
        return self.cwnd
