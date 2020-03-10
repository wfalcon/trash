#!/usr/bin/env python3

import subprocess
import sys

def uname():
	subprocess.call('uname -a', shell=True)

def df():
	subprocess.call('df -h', shell=True)

def error():
	print('для справки введите -h')
	exit

if __name__ == "__main__":
	
	if len(sys.argv) >= 2:
		if sys.argv[1] == '-h':
			print('''--uname информация о системе
--df    место на диске	''')
		elif sys.argv[1] == '--uname':
			uname()
		elif sys.argv[1] == '--df':
			df()
		else:
			error()	
	else:
		error()		    