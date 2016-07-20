#!/usr/bin/env python3

def restart():
	command = "/usr/bin/sudo /sbin/ip link set can0 up type can bitrate 500000"
	import subprocess
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
	print(output)


restart()
