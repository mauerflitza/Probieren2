import threading
import Queue	
import can
import time

q_logs = Queue.Queue()

class Listener(threading.Thread):
	def __init__(self,logfile, end_flag):
		threading.Thread.__init__()
		self.ende=end_flag
		self.logfile = logfile
		self.bus = can.Interface.Bus(can_channel, bustype="socketcan_native")
	def run(): 
		while not self.ende.isSet():
			mesg=bus.recv()
			print(mesg)
			q_logs.put(mesg)
			
			
if __name__ == __main__:
	end_Flag = threading.Event()
	logs = open('test', 'w')
	Listen_Thread = Listener(logs, end_Flag)
	Listen_Thread.start()
	time.sleep(5)
	end_Flag.set()
	
			
		
