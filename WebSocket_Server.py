import signal
import time
import threading
import platform
import Queue
import json
import array
import socket
import sys
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
from tornado.ioloop import PeriodicCallback
import tornado.web
import codecs

import dbcPattern

test=0
# -------------------------------
# Klasse des Websockets
# Periodischer Callback wird erstellt, der die Werte aus der Queue zurueck gibt
# -------------------------------
class WSHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
      return True
    
    def open(self):
        self.callback = PeriodicCallback(self.send_werte, 15)
        self.callback.start()
        print ('Connection open')	
    def send_werte(self):
		self.write_message(str(test))

    def on_message(self, empf):
		  print 'Daten recievied: '

    def on_close(self):
		print 'Connection closed!'
		self.callback.stop()
		
		
def start_Tornado():
  application = tornado.web.Application([(r'/', WSHandler),])
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(8888)
  tornado.ioloop.IOLoop.instance().start()

# Websocket wird wieder geschlossen
def stop_tornado():
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.add_callback(ioloop.stop)
    print "Asked Tornado to exit"

#Test-Main zum Umgang mit der Rueckgabeliste
if __name__ == '__main__':
	#http://stackoverflow.com/questions/5375220/how-do-i-stop-tornado-web-server
	#Notwendig zum Beenden von Tornado
	t_websocket = threading.Thread(target=start_Tornado)
	t_websocket.start()
	
	#Es muss durch die Liste iteriert werden, um die einzelnen Message-Dicts zu bekommen
	#for message in msg_list:
	#	print(message)
	#	print("\n")
	
	for test in range(80):
		time.sleep(0.5)
		print(test)
		
	stop_tornado()
	t_websocket.join()