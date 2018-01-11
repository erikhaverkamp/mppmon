from Phidget22.Devices.DigitalOutput import *
from Phidget22.Net import *


class Multiplexer:
    def __init__(self):
	print('init mp')
        try:
            self.ch0 = DigitalOutput()
            self.ch1 = DigitalOutput()
            self.ch2 = DigitalOutput()
            self.ch3 = DigitalOutput()
            self.ch4 = DigitalOutput()
            self.ch5 = DigitalOutput()
            self.ch6 = DigitalOutput()
            self.ch7 = DigitalOutput()
        except RuntimeError as e:
            print("Runtime Exception %s" % e.details)
            print("Press Enter to Exit...\n")
            readin = sys.stdin.read(1)
            exit(1)

        def ErrorEvent(self, e, eCode, description):
            print("Error %i : %s" % (eCode, description))

        try:
            self.ch0.setOnErrorHandler(ErrorEvent)
            self.ch1.setOnErrorHandler(ErrorEvent)
            self.ch2.setOnErrorHandler(ErrorEvent)
            self.ch3.setOnErrorHandler(ErrorEvent)
            self.ch4.setOnErrorHandler(ErrorEvent)
            self.ch5.setOnErrorHandler(ErrorEvent)
            self.ch6.setOnErrorHandler(ErrorEvent)
            self.ch7.setOnErrorHandler(ErrorEvent)
            self.ch0.setChannel(0)
            self.ch1.setChannel(1)
            self.ch2.setChannel(2)
            self.ch3.setChannel(3)
            self.ch4.setChannel(4)
            self.ch5.setChannel(5)
            self.ch6.setChannel(6)
            self.ch7.setChannel(7)
            print("Waiting for the Phidget DigitalOutput Objects to be attached...")
            self.ch0.openWaitForAttachment(5000)
            self.ch1.openWaitForAttachment(5000)
            self.ch2.openWaitForAttachment(5000)
            self.ch3.openWaitForAttachment(5000)
            self.ch4.openWaitForAttachment(5000)
            self.ch5.openWaitForAttachment(5000)
            self.ch6.openWaitForAttachment(5000)
            self.ch7.openWaitForAttachment(5000)
        except PhidgetException as e:
            print("Phidget Exception %i: %s" % (e.code, e.details))
            print("Press Enter to Exit...\n")
            readin = sys.stdin.read(1)
            exit(1)

    def SelectChannel(self, channel):
        self.ch0.setState(0)
        self.ch1.setState(0)
        self.ch2.setState(0)
        self.ch3.setState(0)
        self.ch4.setState(0)
        self.ch5.setState(0)
        self.ch6.setState(0)
        self.ch7.setState(0)

        if channel < 0:
            return
        if channel == 0:
            self.ch0.setState(1)
        if channel == 1:
            self.ch1.setState(1)
        if channel == 2:
            self.ch2.setState(1)
        if channel == 3:
            self.ch3.setState(1)
        if channel == 4:
            self.ch4.setState(1)
        if channel == 5:
            self.ch5.setState(1)
        if channel == 6:
            self.ch6.setState(1)
        if channel == 7:
            self.ch7.setState(1)

    def close(self):
        try:
            self.ch0.close()
            self.ch1.close()
            self.ch2.close()
            self.ch3.close()
            self.ch4.close()
            self.ch5.close()
            self.ch6.close()
            self.ch7.close()
        except PhidgetException as e:
            print("Phidget Exception %i: %s" % (e.code, e.details))
            print("Press Enter to Exit...\n")
            readin = sys.stdin.read(1)
            exit(1)
        print("Closed DigitalOutput device")
