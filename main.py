import time
from multiplexer import Multiplexer
import bkload
import datetime


DELAY_MINUTES = 1
COMPORT = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0'
t = bkload.IvTracer(COMPORT)


def store_iv_curves(iv1, iv2):
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    with open("./log/" + filename + "_module1.log", "w") as f:
        f.write("voltage\tcurrent\tpower\n")
        for d in iv1:
            f.write("%f\t%f\t%f\n" % (d['voltage'], d['current'], d['power']))
    with open("./log/" + filename + "_module2.log", "w") as f:
        f.write("voltage\tcurrent\tpower\n")
        for d in iv2:
            f.write("%f\t%f\t%f\n" % (d['voltage'], d['current'], d['power']))


mp = Multiplexer()
mp.SelectChannel(-1)
while True:
    time.sleep(DELAY_MINUTES * 20)
    mp.SelectChannel(0)
    time.sleep(10)
    d1 = t.measure_iv(20)
    mp.SelectChannel(1)
    time.sleep(10)
    d2 = t.measure_iv(20)
    mp.SelectChannel(-1)
    store_iv_curves(d1, d2)

