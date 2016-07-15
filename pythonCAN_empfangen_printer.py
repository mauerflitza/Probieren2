#!/usr/bin/env python3

import os
import time
import can 
from threading import Timer

can_channel = 'vcan0'

class myPrinter(can.Listener):
	def __init__(self,open_file):
		print("Printer wurde erstellt")
		self.logfile=open_file
   
	def on_message_received(self, msg):
		self.logfile.write(str(msg))
		self.logfile.write("\n")
		print(msg)

	def __del__(self):
		self.logfile.close()
		print("Prozess abgebrochen")

def ende():
	bus.shutdown()
	logfile.close()
	print("Ende")
	time.sleep(1)
	print("Schliessen")

logfile_path = os.path.join('/home/pi/datalogger/virtual/myrepo/Probieren2/logfiles', time.strftime('%Y%m%d-%H%M'))
logfile = open(logfile_path, 'w')   

bus = can.interface.Bus(can_channel, bustype="socketcan_native")
notifier = can.Notifier(bus, [myPrinter(logfile)])

starttime= time.time()
try:
   while time.time()<(starttime+10):
      time.sleep(0.1)
   ende()
except KeyboardInterrupt:
   ende()
