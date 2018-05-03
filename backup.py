#!/usr/bin/env python
import paramiko
import os
import getopt
import sys


## @package stallions
# This program takes bakup of the virtual machine into a local folder 
# the local and remote path can be set in a dictionary for further use
config = { 
	'backup' : "",
	'local' : ""
}

## function takebackup 
# param1 source path - Path of a folder or file where yo
# param2 destination path
# return 0 if the function runs correctly or 1 if there is an error

# usage takebackup(ctf,beckup) 
def takebackup(source,dest)	
	try:
		os.system("scp -i /home/malay/rsa_new.private -P 1354 -r ctf@54.241.70.152:"+config['backup']source+ " "+config['local']dest)
		print("files backuped")
	except: 
		print("exception raised")
		return 1
	return 0
