import threading
import queue	
import can
import time

q_logs = queue.Queue()

class Listener(threading.Thread):
	def __init__(self, end_flag):
		threading.Thread.__init__(self)
		self.ende=end_flag
		self.logfile = logfile
		self.bus = can.interface.Bus("vcan0", bustype="socketcan_native")
	def run(self): 
		while not self.ende.isSet():
			mesg=self.bus.recv()
			print(mesg)
			q_logs.put(mesg)
			
			
if __name__ == '__main__':
	end_Flag = threading.Event()
	logs = open('test', 'w')
	Listen_Thread = Listener(end_Flag)
	Listen_Thread.start()
	time.sleep(5)
	end_Flag.set()
	
			
		
