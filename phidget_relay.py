import sys
import time 
from Phidget22.Devices.DigitalOutput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *

try:
    ch1 = DigitalOutput()
    ch2 = DigitalOutput()
except RuntimeError as e:
    print("Runtime Exception %s" % e.details)
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)

def ErrorEvent(e, eCode, description):
    print("Error %i : %s" % (eCode, description))

try:
    ch1.setOnErrorHandler(ErrorEvent)
    ch2.setOnErrorHandler(ErrorEvent)
    ch1.setChannel(0);
    ch2.setChannel(1);
    print("Waiting for the Phidget DigitalOutput Object to be attached...")
    ch1.openWaitForAttachment(5000)
    ch2.openWaitForAttachment(5000)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)


while(True):
    print("Setting relay 1")
    ch1.setState(1)
    time.sleep(5)

    print("Closing relay 1")
    ch1.setState(0)
    time.sleep(5)

    print("Setting relay 2")
    ch2.setState(1)
    time.sleep(5)

    print("Closing relay 2")
    ch2.setState(0)
    time.sleep(1)

try:
    ch1.close()
    ch2.close()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1) 
print("Closed DigitalOutput device")
exit(0)
                     


