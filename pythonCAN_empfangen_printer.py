#!/usr/bin/env python3
import time
import can 

can_channel = 'vcan0'

class myPrinter(can.Listener):
	def _init_(self,open_file):
		print("Printer wurde erstellt")
		self.logfile=open_file
   
	def on_message_received(self, msg):
		self.logfile.write(str(msg))
		print(msg)

	def _del_(self):
		print("Prozess abgebrochen")
		
logfile=open('logfile', 'w')   
bus = can.interface.Bus(can_channel, bustype="socketcan_native")
notifier = can.Notifier(bus, [myPrinter(logfile)])

try:
   while True:
      time.sleep(0.1)
except KeyboardInterrupt:
   bus.shutdown()
   logfile.close()
   print("Ende")
   time.sleep(1)
   print("Schliessen")
