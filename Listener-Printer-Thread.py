import threading
import queue	
import can
import time

q_logs = queue.Queue()

class Listener(threading.Thread):
	def __init__(self, end_flag):
		threading.Thread.__init__(self)
		self.ende=end_flag
		self.bus = can.interface.Bus("vcan0", bustype="socketcan_native")
	def run(self): 
		while not self.ende.isSet():
			mesg=self.bus.recv(0)
#			print(mesg)
			q_logs.put(mesg)


class Printer(threading.Thread):
	def __init__(self,logfile, end_flag):
		threading.Thread.__init__(self)
		self.ende=end_flag
		self.logfile = logfile
		print(logfile)
	def run(self): 
		while not self.ende.isSet():
			while not q_logs.empty():
				mesg=q_logs.get()
#				print(mesg)
				if mesg != None:
					self.logfile.write(str(mesg))
					self.logfile.write("\n")
			
if __name__ == '__main__':
	end_Flag = threading.Event()
	logs = open('test', 'w')
	
	Listen_Thread = Listener(end_Flag)
	Print_Thread = Printer(logs,end_Flag)
	
	Listen_Thread.start()
	Print_Thread.start()
	
	time.sleep(10)
	end_Flag.set()	
	Print_Thread.join()
	logs.close()