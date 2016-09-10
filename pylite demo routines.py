#routine to provide test input to esp8266

import pyb
timer = pyb.Timer(2, freq=50)
ch2 = timer.channel(4, pyb.Timer.PWM, pin=pyb.Pin.board.X2, pulse_width_precent=50)


#routine to test seatalk bitbang

import pyb
stream = pyb.UART(2, 4800, bits=9)
while True:
    if stream.any():
        d = stream.read(2)
        print("{0}  {1}".format(d[0], d[1]))