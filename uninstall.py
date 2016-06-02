#!/usr/bin/env python
import os
import sys
import getpass
import termcolor

# VARIABLES #
user = getpass.getuser()
ipath = ("/usr/haxxor")
haxxor = ("/usr/bin/haxxor")
if(user == 'root'):
	print colored("[*] Running as root", "yellow")
else:
	print colored("[!] Must run as root", "red")
	sys.exit(0)
if(os.path.exists(ipath)):
	call("rm -r " + ipath, shell=True)
else:
	print colored("[!] Could not find %s" % ipath, "red")
	sys.exit(0)
if(os.path.isfile(haxxor)):
	call("rm " + haxxor, shell=True)
else:
	print colored("[!] Coudl not find %s" % haxxor, "red")
	sys.exit(0)

