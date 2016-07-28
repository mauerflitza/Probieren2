#!/usr/bin/python3

import os
import cgi, cgitb
import codecs

#own packages
import dbcPattern


def main(): # NEW except for the call to processInput
	form = cgi.FieldStorage()      # standard cgi script lines to here!
    
    # use format of next two lines with YOUR names and default data
	filedata = form['upload']
	contents = processInput(numStr1, numStr2)   # process input into a page
	print(contents)
    
def processInput(numStr1, numStr2):  
	'''Process input parameters and return the final page as a string.'''
	if filedata.file: #field really is an upload
		#codecs, da es sonst bei umlauten fehler gibt
		dbcfile=codecs.open(filedata.file, 'r', 'iso 8859-1')
		#msg_list=[{mesg1}{mesg2}{mesg3}{...}]
		#Messages  has numbered dicts signals in them
		msg_list = dbcPattern.dbcDataReader(dbcfile)
		dbcfile.close
	return createHTML(sig_num, sig_list).format(**locals())
	
def createHTML(sig_num, sig_list):
	signale=""
	html_string = """
	<!DOCTYPE html>
	
	<html>
		<Title>The Time Now</Title>
		<body>
		<div class="dropdown">
			<button class="dropbtn">Dropdown</button>
			<div class="dropdown-content">
			"""
	for sig in range(signum):
		signale.append('<a href="#">{sig_nme}</a>\n'.format(sig_list))
	html_string.append(signale)
	html_string.append("</div></div></body></html>")
	return html_string
			


try:   # NEW
	cgitb.enable()
	print("Content-Type: text/html;charset:UTF-8")   # say generating html
	print("\n\n")
	main() 
except:
    cgi.print_exception()                 # catch and print errors
