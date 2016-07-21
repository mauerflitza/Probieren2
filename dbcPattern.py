import re
import time



#*************************************************
#function to read a dbc file and return list with all message informations
#returns a list with dictionaries of the messages with all the signals
#*************************************************
def dbcPattern(dbcPath):
	testline="BO_ 37 engine: 2 Motor"
	testline2=' SG_ e_temp : 0|8@1- (1,3) [2|4] "temp"  Reciever'
	filename=dbcPath
	liste_msg = ['ID','DLC']
	liste_signals=['sig_name','Startbit','Length','Sign','factor','offset','min','max','unit']
	diction = {}
	flag=0
	sig_count=0
	return_list=[]

	file=open(filename, 'r')
	line=file.readline()
	for line in file:
		#Regular expressions to find all the important information in the dbc file
		match=re.match('BO_ (?P<ID>\d+) \w+: (?P<DLC>[0-8]) \w+', line)
		match2= re.match('\s*SG_ (?P<sig_name>\w+)\s*:'
						 '\s*(?P<Startbit>[0-8]+)\|(?P<Length>[0-8]+)@\d(?P<Sign>[+-])'
						 '\s*\((?P<factor>\d+),(?P<offset>\d+)\)'
						 '\s*\[(?P<min>\d+)\|(?P<max>\d+)\]'
						 '\s*"(?P<unit>\w*)"\s*\w*',line)
		#Message-Dict wird erstellt mti allen zugehörigen signalen
		
		if match:		#Match is true when a group is found
			for item in liste_msg:
				diction[item]=match.group(item)
			flag=0
		elif match2:
			#sig count für das durchzählen der signale
			diction[sig_count] = {}
			for item in liste_signals:
				diction[sig_count][item]=match2.group(item)
			flag=1
			sig_count=sig_count+1
		elif not (match2 or match):
			if flag==1:
				diction['sig_count'] = sig_count
				sig_count=0
				return_list.append(diction)
			flag=2
			diction={}						
	#print(return_list)
	return return_list		



#Test-Main zum Umgang mit der Rückgabeliste
if __name__ == '__main__':
	dbcPath='C:/Users/fte8fe/Documents/Raspberry Pi Development Kit/CAN-Communication/test2.dbc'
	msg_list=dbcPattern(dbcPath)
	#Es muss durch die Liste iteriert werden, um die einzelnen Message-Dicts zu bekommen
	for message in msg_list:
		for j in range(message['sig_count']):
			print(message[j]['sig_name'])

