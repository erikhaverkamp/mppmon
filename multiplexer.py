import sys
import time 
from Phidget22.Devices.DigitalOutput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *

# call multiplexer by using with statement:
#
#	with Multiplexer() as mp:
#		mp.SelectChannel(3)


class Multiplexer:
	def __init__(self):
		try:
			ch0 = DigitalOutput()
			ch1 = DigitalOutput()
			ch2 = DigitalOutput()
			ch3 = DigitalOutput()
			ch4 = DigitalOutput()
			ch5 = DigitalOutput()
			ch6 = DigitalOutput()
			ch7 = DigitalOutput()
		except RuntimeError as e:
			print("Runtime Exception %s" % e.details)
			print("Press Enter to Exit...\n")
			readin = sys.stdin.read(1)
			exit(1)

		def ErrorEvent(self, e, eCode, description):
			print("Error %i : %s" % (eCode, description))

		try:
			ch0.setOnErrorHandler(ErrorEvent)
			ch1.setOnErrorHandler(ErrorEvent)
			ch2.setOnErrorHandler(ErrorEvent)
			ch3.setOnErrorHandler(ErrorEvent)
			ch4.setOnErrorHandler(ErrorEvent)
			ch5.setOnErrorHandler(ErrorEvent)
			ch6.setOnErrorHandler(ErrorEvent)
			ch7.setOnErrorHandler(ErrorEvent)
			ch0.setChannel(0);
			ch1.setChannel(1);
			ch2.setChannel(2);
			ch3.setChannel(3);
			ch4.setChannel(4);
			ch5.setChannel(5);
			ch6.setChannel(6);
			ch7.setChannel(7);
			print("Waiting for the Phidget DigitalOutput Objects to be attached...")
			ch0.openWaitForAttachment(5000)
			ch1.openWaitForAttachment(5000)
			ch2.openWaitForAttachment(5000)
			ch3.openWaitForAttachment(5000)
			ch4.openWaitForAttachment(5000)
			ch5.openWaitForAttachment(5000)
			ch6.openWaitForAttachment(5000)
			ch7.openWaitForAttachment(5000)
		except PhidgetException as e:
			print("Phidget Exception %i: %s" % (e.code, e.details))
			print("Press Enter to Exit...\n")
			readin = sys.stdin.read(1)
			exit(1)

	def __enter__(self):
        	return self		
			
			
	def SelectChannel(self, channel):
		ch0.setState(0)
		ch1.setState(0)
		ch2.setState(0)
		ch3.setState(0)
		ch4.setState(0)
		ch5.setState(0)
		ch6.setState(0)
		ch7.setState(0)
		
		if channel == 0:
			ch0.setState(1)
		if channel == 1:
			ch1.setState(1)
		if channel == 2:
			ch2.setState(1)
		if channel == 3:
			ch3.setState(1)
		if channel == 4:
			ch4.setState(1)
		if channel == 5:
			ch5.setState(1)
		if channel == 6:
			ch6.setState(1)
		if channel == 7:
			ch7.setState(1)
		

	def __exit__(self, exc_type, exc_value, traceback):
		try:
			ch0.close()
			ch1.close()
			ch2.close()
			ch3.close()
			ch4.close()
			ch5.close()
			ch6.close()
			ch7.close()
		except PhidgetException as e:
			print("Phidget Exception %i: %s" % (e.code, e.details))
			print("Press Enter to Exit...\n")
			readin = sys.stdin.read(1)
			exit(1) 
		print("Closed DigitalOutput device")
	
						 


