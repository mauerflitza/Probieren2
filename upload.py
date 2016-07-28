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
	if filedata.file:
		contents = processInput(filedata.file)   # process input into a page
		print(contents)
    
def processInput(file):  
	sig_num=0
	sig_list=[]
	'''Process input parameters and return the final page as a string.'''
	if file: #field really is an upload
		#codecs, da es sonst bei umlauten fehler gibt
		#msg_list=[{mesg1}{mesg2}{mesg3}{...}]
		#Messages  has numbered dicts signals in them
		msg_list = dbcPattern.dbcDataReader(file)
		for message in msg_list:
			for j in range(message['sig_count']):
				sig_num=sig_num+1
				sig_list.append(message[j]['sig_name'])
	return createHTML(sig_num, sig_list)
	
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
	for sig_name in sorted(sig_list, key=str.lower):
		signale+='<a href="#">{sig_name}</a>\n'.format(**locals())
	html_string+=signale
	html_string+="</div></div></body></html>"
	return html_string
			


try:   # NEW
	cgitb.enable()
	print("Content-Type: text/html;charset:UTF-8")   # say generating html
	print("\n\n")
	main() 
except:
    cgi.print_exception()                 # catch and print errors
