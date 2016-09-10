from machine import Pin, Timer, time_pulse_us
from time import sleep
# TODO from nmeagenerator import RPM

class Tachy:

    def __init__(self):
        self.pulse_us = 0
        self.RPM = 0
        self.engine_on = False
        self.tach_pin = Pin(5, Pin.IN)  # GPIO 5 D1 on WEMOS Board

    def update(self):
        try:
            while self.tach_pin.value()==1:
                pass
            self.pulse_us = time_pulse_us(self.tach_pin, 1, 100000)
            self.RPM = 5000000 / self.pulse_us
            self.engine_on = True
        except:
            self.engine_on = False
            self.RPM = 0

    @property
    def output(self):
        self.update()
        return self.RPM #TODO RPM(self.RPM).msg ## output sentence

a=Tachy()

while 1:
    print(a.output)
    sleep(0.5)

