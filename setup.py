#!/usr/bin/env python
import os
import sys
import commands
try:
	import getpass
except ImportError:
	print("You are missing getpass")
	print("Run 'pip install getpass' to install it")
	sys.exit(0)
from subprocess import call
try:
	from termcolor import colored
except ImportError:
	print("You are missing termcolor")
	print("Type 'pip install termcolor' to install it")
	sys.exit(0)
# VARIABLES #
user = getpass.getuser()
uid = os.getuid()
wd = commands.getoutput("pwd")
# PATH VARIABLES #
ipath = ("/usr/haxxor")
path_set = ("/usr/haxxor/fuzzers ")
path_set += ("/usr/haxxor/modules ")
path_set += ("/usr/haxxor/scanners ")
path_set += ("/usr/haxxor/privesc")
# SECOND WAVE #
path_set1 = ("/usr/haxxor/fuzzers/windows ")
path_set1 += ("/usr/haxxor/fuzzers/mac_os ")
path_set1 += ("/usr/haxxor/fuzzers/linux ")
path_set1 += ("/usr/haxxor/fuzzers/misc ")
# THIRD WAVE #
path_set3 = ("/usr/haxxor/modules/scanning ")
path_set3 += ("/usr/haxxor/modules/dns ")
path_set3 += ("/usr/haxxor/modules/enumeration ")
# FINAL WAVE #
path_set4 = ("/usr/haxxor/fuzzers/windows/browser ")
path_set4 += ("/usr/haxxor/fuzzers/windows/os ")
path_set4 += ("/usr/haxxor/fuzzers/mac_os/browser ")
path_set4 += ("/usr/haxxor/fuzzers/mac_os/os ")
path_set4 += ("/usr/haxxor/fuzzers/linux/browser ")
path_set4 += ("/usr/haxxor/fuzzers/linux/os ")
path_set4 += ("/usr/haxxor/fuzzers/misc/browser ")
path_set4 += ("/usr/haxxor/fuzzers/misc/os ")
# MISC #
haxxor_file = ("%s/haxxor.py" % wd)
finished_haxxor = ("/usr/bin/haxxor")
# CHECKS #
if(user == "root"):
	print colored("[*] Running as root", "yellow")
	call("clear", shell=True)
else:
	print colored("[!] MUST RUN AS ROOT", "red")
if(os.path.exists(ipath)):
	print colored("[!] Haxxor already setup", "red")
	sys.exit(0)
else:
	print("")
print colored("[*] If not in haxxor download location, change to it")
start_directory = raw_input("Current path [including /'s]: ")
if(wd == start_directory):
	print colored("[*] In correct directory", "yellow")
	call("clear", shell=True)
else:
	print colored("[!] Your input and pwd don't match, fix that", "red")
	sys.exit(0)

def create_directories():
	try:
		call("mkdir " + ipath + " && mkdir " + path_set, shell=True)
		call("mkdir " + path_set1, shell=True)
		call("mkdir " + path_set3, shell=True)
		call("mkdir " + path_set4, shell=True)
		print colored("[*] Created", "yellow")
	except KeyboardInterrupt:
		if(os.path.exists(ipath)):
			call("rm -r " + ipath, shell=True)
		else:
			call("clear", shell=True)
			sys.exit(0)
create_directories()

def move_haxxor():
	try:
		if(os.path.isfile(haxxor_file)):
			call("cp haxxor.py haxxor && chmod +x haxxor && mv haxxor /usr/bin", shell=True)
		else:
			print colored("[!] Could not find haxxor.py, fix that", "red")
			call("rm -r " + ipath, shell=True)
			sys.exit(0)
	except KeyboardInterrupt:
		call("rm -r " + ipath, shell=True)
		if(os.path.isfile(finished_haxxor)):
			call("rm " + finished_haxxor, shell=True)
		else:
			sys.exit(0)
move_haxxor()

def start_services():
	try:
		# PRE CHECK FOR SERVICES #
		service_precheck = commands.getoutput("ps -A")
		if("apache2" in service_precheck):
			print colored("[*] Apache2 already started")
		else:
			service_apache2 = commands.getoutput("service apache2 start")
			if("service not found" in service_apache2):
				print colored("[!] Run apt-get install apache2 to install it", "red")
				call("rm -r "+ ipath + " && rm " + finished_haxxor, shell=True)
				sys.exit(0)
			else:
				print colored("[*] Apache2 started with no issue")
	except KeyboardInterrupt:
		call("rm -r " + ipath + " && rm " + finished_haxxor, shell=True)
		service_postcheck = commands.getoutput("ps -A")
		if("apache2" in service_postcheck):
			call("service apache2 stop", shell=True)
		else:
			sys.exit(0)
start_services()

start_haxxor_now = raw_input("[?] Start haxxor now [yes/no]: ")
if(start_haxxor_now == "yes"):
	call("clear && haxxor", shell=True)
else:
	print colored("[*] Thank you for installing haxxor", "yellow")
	sys.exit(0)

