#!/usr/bin/python3
import os
import cgi, cgitb
import re
import pickle

#own packages
import dbcPattern


def dbc_main(): # NEW except for the call to processInput
	form = cgi.FieldStorage()      # standard cgi script lines to here!
    
    # use format of next two lines with YOUR names and default data
	filedata = form['upload']
	if filedata.file:
		if re.match('\w+\.dbc', form.filename):
			contents, msg_list = processInput(filedata.file)   # process input into a page
			print(contents)
		else: break
		return msg_list
    return -1
def processInput(file):  
	sig_num=0
	sig_list=[]
	'''Process input parameters and return the final page as a string.'''
	if file: #field really is an upload
		
		#msg_list=[{mesg1}{mesg2}{mesg3}{...}]
		#Messages  has numbered dicts signals in them
		msg_list = dbcPattern.dbcDataReader(file)
		for message in msg_list:
			for j in range(message['sig_count']):
				sig_num=sig_num+1
				sig_list.append(message[j]['sig_name'])
	return createHTML(sig_num, sig_list),msg_list
	
def createHTML(sig_num, sig_list):
	signale=""
	i=0
	print(sig_num)
	html_string = """
	<!DOCTYPE html>
	
	<html>
		<Title>Logger_Setup</Title>
		<body>
	    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
	        <ul class="nav navbar-nav">
		        <li class="dropdown">
		            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Two Column <b class="caret"></b></a>
		            <ul class="dropdown-menu multi-column columns-2">
			            <div class="row">
				            <li class="col-sm-6">
					            <ul class="multi-column-dropdown">
			"""
	for sig_name in sorted(sig_list, key=str.lower):
		signale+='<li><a href="#">{sig_name}</a></li>\n'.format(**locals())
		i+=1
		if i>sig_num/2:
			break
	html_string+=signale
	html_string+="""
	</li>
	<li class="col-sm-6">
	<ul class="multi-column-dropdown">
	"""
	for sig_name2 in sorted(sig_list, key=str.lower):
		signale+='<li><a href="#">{sig_name2}</a></li>\n'.format(**locals())
	html_string+="</ul></li></div></ul></li></ul></div>"
	html_string+="""
	<!-------------------- JS -------------------->
	<script type="text/javascript" src="js/jQuery.js"></script>
	<script type="text/javascript" src="js/Dropdown.js"></script>
	</body>
	</html> 
	"""
	return html_string
			

#Muss später ins Hauptprogramm kopiert werden
try:   # NEW
	cgitb.enable()
	print("Content-Type: text/html;charset:UTF-8")   # say generating html
	print("\n\n")
	msg_list=dbc_main() 
	with open('testdump', 'wb') as f:
		pickle.dump(my_list, f)
except:
    cgi.print_exception()  # catch and print errors
	
