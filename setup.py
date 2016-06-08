#!/usr/bin/env python
import os
import sys
try:
	from termcolor import colored
except ImportError:
	print("[!] You are missing termcolor")
	print("[!] Type 'pip install termcolor' to install it")
	sys.exit(0)
try:
	import getpass
except ImportError:
	print("[!] You are missing getpass")
	print("[!] Type 'pip install getpass' to install it")
import commands
from subprocess import call
# VARIABLES #
user = getpass.getuser()
uid = os.getuid()
wd = commands.getoutput("pwd")
# PATHS #
ipath = ("/usr/haxxor")
# CREATED DIRECTORIES #
pathset = ("%s/modules " % wd)
pathset += ("%s/fuzzers " % wd)
pathset += ("%s/scanning " % wd)
pathset += ("%s/privesc " % wd)
# MISC #
haxxor_file = ("haxxor.py")
finished_haxxor = ("/usr/bin/haxxor")
if(user == 'root'):
	print colored("[*] Running as root", "yellow")
else:
	print colored("[!] MUST RUN AS ROOT", "red")
	sys.exit(0)
try:
	print colored("[!] Make sure you are in the haxxor directory", "red")
	wd_check = raw_input("haxxor path [eg /root/haxxor-framework]: ")
except KeyboardInterrupt:
	sys.exit(0)
if(os.path.exists(ipath)):
	print colored("[!] Directories already created", "green")
	sys.exit(0)
else:
	pass
if(wd_check == wd):
	print colored("[*] In correct directory", "yellow")
else:
	print colored("[!] MUST BE IN HAXXOR DIRECTORY", "red")
	sys.exit(0)
if(haxxor_file in wd):
	print colored("[*] Haxxor file found", "green")
else:
	print colored("[!] COULD NOT FIND HAXXOR.PY", "red")
	sys.exit(0)
call("clear", shell=True)
def move_directories():
	try:
		call("mkdir " + ipath, shell=True)
		call("mv " + pathset + " " + ipath, shell=True)
		print colored("[*] Created", "green")
	except KeyboardInterrupt:
		if(os.path.exists(ipath)):
			call("rm -r " + ipath, shell=True)
			sys.exit(0)
		else:
			sys.exit(0)
move_directories()

def move_haxxor():
	try:
		call("cp haxxor.py haxxor && chmod +x haxxor && mv haxxor /usr/bin", shell=True)
		if(os.path.isfile(finished_haxxor)):
			print colored("[*] haxxor successfully moved", "green")
		else:
			print colored("[!] Failed to move haxxor", "red")
			call("rm -r " + ipath, shell=True)
			sys.exit(0)
	except KeyboardInterrupt:
		call("rm -r " + ipath, shell=True)
		if(os.path.isfile(finished_haxxor)):
			call("rm " + finished_haxxor, shell=True)
			sys.exit(0)
		else:
			sys.exit(0)
move_haxxor()

def start_haxxor():
	try:
		start_haxxor_now = raw_input("Start haxxor now [yes/no]: ")
		if(start_haxxor_now == 'yes'):
			call("haxxor", shell=True)	
		else:
			sys.exit(0)
	except KeyboardInterrupt:
		sys.exit(0)
start_haxxor()
