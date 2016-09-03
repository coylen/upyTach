from machine import Pin, Timer, disable_irq, enable_irq
from time import sleep_us, ticks_us, ticks_diff

class Seatalker:
    # 55 and AA are test values
    def __init__(self, gpio):
        self.Tx = Pin(gpio, Pin.OUT, 1)
        self.first = True

    def send(self, byts):
        self.first = True
        for byt in byts:
            self.sendframe(byt)

    def send2(self, byts):
        self.first = True
        for byt in byts:
            self.sendframe(byt)

    def sendframe(self,byt):
        temp = disable_irq()
        # start bit
        self.bitbang(0)

        # send byte
        for x in range(0,8):
            self.bitbang((byt >> x) & 0x1)

        # command bit
        if self.first:
            self.bitbang(1)
            self.first = False
        else:
            self.bitbang(0)

        # stop bit
        self.bitbang(1)

        enable_irq(temp)

    def bitbang(self, b):
        self.Tx.value(b)
        sleep_us(208)


    def sendframe2(self, byt):
        temp = disable_irq()
        tim = ticks_us()
        # start bit
        self.bitbang2(0, tim, 208)

        # send byte
        for x in range(0, 8):
            self.bitbang2((byt >> x) & 0x1, tim,  208 * (x + 2))

        # command bit
        if self.first:
            self.bitbang2(1, tim, 2083)
            self.first = False
        else:
            self.bitbang2(0, tim, 2083)

        # stop bit
        self.bitbang2(1, tim, 2292)

        enable_irq(temp)


    def bitbang2(self, b, start, diff):
        self.Tx.value(b)
        while (ticks_diff(start, ticks_us()) < diff):
            pass
