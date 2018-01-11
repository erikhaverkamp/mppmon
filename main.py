import time
from multiplexer import Multiplexer
import bkload
import datetime


DELAY_MINUTES = 1
IV_POINTS = 128
IV_SWEEPTIME = 5        #seconds
COMPORT = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0'
print "starting IV"
t = bkload.IvTracer(COMPORT)
print "stop IV"

def store_iv_curves(iv, timestamp):
    with open("/home/pi/powerlogs/" + timestamp.strftime("%Y%m%d%H%M%S"), "w") as f:
        #f.write("timestamp UTC: ", timestamp, "\n")
        #f.write("timestamp epoch: ", calendar.timegm(timestamp), "\n")
        f.write("voltage\tcurrent\tpower\n")
        for d in iv:
            f.write("%f\t%f\t%f\n" % (d['voltage'], d['current'], d['power']))
        f.close()

mp = Multiplexer()
mp.SelectChannel(-1)
while True:
    time.sleep(DELAY_MINUTES * 30)
    
    mp.SelectChannel(0)
    time.sleep(10)
    timestamp = datetime.datetime.now()
    d1 = t.measure_iv(IV_POINTS, IV_SWEEPTIME/IV_POINTS)
    store_iv_curves(d1,timestamp)
    
    mp.SelectChannel(1)
    time.sleep(10)
    timestamp = datetime.datetime.now()
    d2 = t.measure_iv(IV_POINTS, IV_SWEEPTIME/IV_POINTS)
    mp.SelectChannel(-1)
    store_iv_curves(d2,timestamp)

