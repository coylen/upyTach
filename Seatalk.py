from machine import Pin, Timer, disable_irq, enable_irq
from time import sleep_us, ticks_us, ticks_diff


class Seatalker:
    # 55 and AA are test values
    def __init__(self, gpio=5):
        self.Tx = Pin(gpio, Pin.OUT, 1)
        self.first = True

    def send(self, byts):
        if self.Tx.value() == 1:
            tim = ticks_us()
            while ticks_diff(tim,ticks_us()) < 2080:
                if self.Tx.value() == 0:
                    raise OSError #TODO need custom error to say trffic on Line
        self.first = True
        for byt in byts:
            self.sendframe(byt)

    def sendframe(self, byt):
        temp = disable_irq()
        tim = ticks_us()
        # start bit
        self.bitbang(0, tim, 208)

        # send byte
        for x in range(0, 8):
            self.bitbang((byt >> x) & 0x1, tim,  208 * (x + 2))

        # command bit
        if self.first:
            self.bitbang(1, tim, 2083)
            self.first = False
        else:
            self.bitbang(0, tim, 2083)

        # stop bit
        self.bitbang(1, tim, 2292)

        enable_irq(temp)

    def bitbang(self, b, start, diff):
        self.Tx.value(b)
        while ticks_diff(start, ticks_us()) < diff:
            pass

    #TODO introduce seatalk send - currently in testing
        # need to check length on the fly and return full sentences?
        # or read and discard?
        # need to check autopilot to see what it outputs
        # can use pylite initially to read
        # logger to see if stream - stop - stream or
        # data - pause - data - pause etc

class bbUART:
    def __init__(self, gpio=5):
        self.Tx = Pin(gpio, Pin.OUT, 1)

    def send(self, byts):
        for byt in byts:
            self.sendframe(byt)

    def sendframe(self, byt):
        temp = disable_irq()
        tim = ticks_us()
        # start bit
        self.bitbang(0, tim, 208)

        # send byte
        for x in range(0, 8):
            self.bitbang((byt >> x) & 0x1, tim, 208 * (x + 2))

        # stop bit
        self.bitbang(1, tim, 2083)

        enable_irq(temp)

    def bitbang(self, b, start, diff):
        self.Tx.value(b)
        while ticks_diff(start, ticks_us()) < diff:
            pass
