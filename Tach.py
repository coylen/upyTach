from machine import Pin, Timer, time_pulse_us
from time import sleep
# TODO from nmeagenerator import RPM

class Tachy:

    def __init__(self):
        self.pulse_us = 0
        self.RPM = 0
        self.engine_on = False
        self.tach_pin = Pin(5, Pin.IN)  # GPIO 5 D1 on WEMOS Board

        # self.tach_pin.irq(Pin.IRQ_RISING, handler=lambda x: self.count += 1)
        self.timer = Timer(-1)
        self.timer.init(period=1000, mode=Timer.PERIODIC, callback=self.total)

    def total(self):
        try:
            self.pulse_us = time_pulse_us(self.tach_pin, 1, timout_us=100000)
        except:
            self.engine_on = False
        self.RPM = 5000000/self.pulse_us
        if self.RPM > 0:
            self.engine_on = True
        else:
            self.engine_on = False

    @property
    def output(self):
        return #TODO RPM(self.RPM).msg ## output sentence

    #TODO alternative function usinge machine.time_pulse_us less reliant on interupts??
a=Tachy()

while 1:
    print(a.RPM)
    sleep(0.5)