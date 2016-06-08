#!/usr/bin/env python
import os, sys, getpass, commands
from subprocess import call
from termcolor import colored 
# VARIABLES #
user = getpass.getuser()
ipath = ("/usr/haxxor")
finished_haxxor = ("/usr/bin/haxxor")
if(user == 'root'):
	print colored("[*} Running as root", "yellow")
else:
	print colored("[!] Not running as root', "red")
	sys.exit(0)
if(os.path.exists(ipath)):
	call("rm -r " + ipath, shell=True)
else:
	print colored("[!] Could not find %s" % ipath, "red")
if(os.path.isfile(finished_et)):
	call("rm " + finished_haxxor, shell=True)
else:
	print colored("[!] Could not find %s" % finished_haxxor, "red")

