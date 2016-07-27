#!/usr/bin/python3

import os
import cgi, cgitb

cgitb.enable()
print ("Content-Type: text/html")
print ()
print ('start!')
form = cgi.FieldStorage()
filedata = form['upload']
if filedata.file: #field really is an upload
	for line in filedata.file:
		print(line)


