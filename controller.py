from Tach import Tachy
from time import sleep


def setup():
    import network
    wl = network.WLAN(network.STA_AP)
    wl.active(False)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('Jambo', '')


def con_socket():
    import socket
    s = socket.socket()
    s.connect(('192.168.0.10', 11111))  # check address
    return s


def run(test=False):
    # initialisation
    revs = Tachy()

    while True:
        # upload engine data is valid
        if revs.engine_on:
            try:
                s = con_socket()
                s.send(revs.output)
            except:
                pass
            finally:
                s.close()

        # if NMEA incoming data? send to AP

        # if Seatalk data send to AP

        sleep(1)
