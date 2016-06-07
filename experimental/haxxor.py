#!/usr/bin/env python
import os
import sys
import getpass
import commands
from termcolor import colored
from subprocess import call
import rlcompleter
import readline
import atexit
# VARIABLES #
user = getpass.getuser()
# PATHS #
finished_haxxor = ("/usr/bin/haxxor")
ipath = ("/usr/haxxor")
# LIST #
fuzzer1 = int(commands.getoutput("ls -1 /usr/haxxor/fuzzers/windows/browser |wc -l"))
fuzzer2 = int(commands.getoutput("ls -1 /usr/haxxor/fuzzers/windows/os |wc -l"))
fuzzer3 = int(commands.getoutput("ls -1 /usr/haxxor/fuzzers/linux/browser |wc -l"))
fuzzer4 = int(commands.getoutput("ls -1 /usr/haxxor/fuzzers/linux/os |wc -l"))
fuzzer5 = int(commands.getoutput("ls -1 /usr/haxxor/fuzzers/mac_os/browser |wc -l "))
fuzzer6 = int(commands.getoutput("ls -1 /usr/haxxor/fuzzers/mac_os/os |wc -l"))
fuzzer7 = int(commands.getoutput("ls -1 /usr/haxxor/fuzzers/misc/browser |wc -l"))
fuzzer8 = int(commands.getoutput("ls -1 /usr/haxxor/fuzzers/misc/os |wc -l"))
list_fuzzers = int(fuzzer1 + fuzzer2 + fuzzer3 + fuzzer4 + fuzzer5 + fuzzer6 + fuzzer7 + fuzzer8)
module1 = int(commands.getoutput("ls -1 /usr/haxxor/modules/scanning |wc -l"))
module2 = int(commands.getoutput("ls -1 /usr/haxxor/modules/dns |wc -l"))
module3 = int(commands.getoutput("ls -1 /usr/haxxor/modules/enumeration |wc -l"))
list_modules = int(module1 + module2 + module3)
list_scanners = int(commands.getoutput("ls -1 /usr/haxxor/scanners |wc -l"))
list_privesc = int(commands.getoutput("ls -1 /usr/haxxor/privesc |wc -l"))
if(user == "root"):
        print colored("[*] Running as root", "yellow")
else:
        print colored("[!] MUST RUN AS ROOT", "red")
        sys.exit(0)
if(os.path.exists(ipath)):
        print colored("[*] Directories exist", "yellow")
else:
        print colored("[!] Directories not found", "red")
        sys.exit(0)
call("clear", shell=True)
#
#
#
#
#
#
#

def banner():
        print colored("------------------------------------", "blue")
        print colored(" _                                  ", "blue")
        print colored("| |                                 ", "blue")
        print colored("| |__  _____ _   _ _   _ ___   ____ ", "blue")
        print colored("|  _ \(____ ( \ / | \ / ) _ \ / ___)", "blue")
        print colored("| | | / ___ |) X ( ) X ( |_| | |    ", "blue")
        print colored("|_| |_\_____(_/ \_|_/ \_)___/|_|    ", "blue")
        print colored("------------------------------------", "blue")
        print colored("[ [{}] fuzzers  [{}] modules ]".format(list_fuzzers, list_modules), "red")
        print colored("[ [{}] scanners [{}] privesc ]".format(list_scanners, list_privesc), "red")
banner()
print colored("[1] fuzzers", "blue")
print colored("[2] modules", "blue")
print colored("[3] scanners", "blue")
print colored("[4] privesc", "blue")
print colored("[5] help", "blue")
print colored("[6] donate", "blue")
print colored("[7] exit", "blue")

def main():
	try:
		def fuzzers():
			try:
				print colored("[1] Windows", "blue")
				print colored("[2] Mac", "blue")
				print colored("[3] Linux", "blue")
				print colored("[4] Misc", "blue")
				print colored("[5] back", "blue")
				while True:
					usefuzzer = raw_input("[haxxor/fuzzers] => ")
					if(usefuzzer == '1'):
						print colored("[1] Browser", "blue")
						print colored("[2] OS", "blue")
						print colored("[3] back", "blue")
						while True:
							usefuzzer1 = raw_input("[haxxor/fuzzers/Windows] => ")
							if(usefuzzer1 == '1'):
								call("ls -1 /usr/haxxor/fuzzers/windows/browser", shell=True)
								while True:
									usefuzzer1_1 = raw_input("[haxxor/fuzzers/Windows/Browser] => ")
									mytuple1_1 = usefuzzer1_1.partition(" ")
									if(mytuple1_1[0] == 'use'):
										call("python " + mytuple1_1[2], shell=True)
									elif(mytuple1_1[0] == 'back'):
										break
									elif(mytuple1_1[0] == 'exit'):
										break
									else:
										print colored("[!] Unknown option", "red")
							elif(usefuzzer1 == '2'):
								call("ls -1 /usr/haxxor/fuzzers/windows/os", shell=True)
								while True:
									usefuzzer1_2 = raw_input("[haxxor/fuzzers/Windows/OS] => ")
									mytuple1_2 = usefuzzer1_2.partition(" ")
									if(mytuple1_2[0] == 'use'):
										call("python " + mytuple1_2[2], shell=True)
									elif(mytuple1_2[0] == 'exit'):
										sys.exit(0)
									elif(mytuple[0] == 'back'):
										break
									else:
										print colored("[!] Unknown option", "red")	
							elif(usefuzzer1 == '3'):
								break
							else:
								print colored("[!] Unknown error", "red")
					elif(usefuzzer == '2'):
						print colored("[1] Browser", "blue")
						print colored("[2] OS", "blue")
						print colored("[3] back", "blue")
						while True:
							usefuzzer2_1 = raw_input("[haxxor/fuzzers/mac] => ")
							if(usefuzzer2_1 == '1'):
								call("ls -1 /usr/haxxor/fuzzers/mac/browser", shell=True)
								while True:
									usefuzzer2_1_1 = raw_input("[haxxor/fuzzers/mac/Browser] => ")
									mytuple2_1 = usefuzzer2_1_1.partition(" ")
									if(mytuple2_1[0] == 'use'):
										call("python " + mytuple2_1[2], shell=True)
									elif(mytuple2_1[0] == 'back'):
										break
									elif(mytuple2_1[0] == 'exit'):
										sys.exit(0)
									else:
										print colored("[!] Unknown command")
							elif(usefuzzer2_1 == '2'):
								call("ls -1 /usr/haxxor/fuzzers/mac/os", shell=True)
								while True:
									usefuzzer2_1_2 = raw_input("[haxxor/fuzzers/mac/OS] => ")
									mytuple2_2 = usefuzzer2_1_2.partition(" ")
									if(mytuple2_2[0] == 'use'):
										call("python " + mytuple2_2[2], shell=True)
									elif(mytuple[0] == 'back'):
										break
									elif(mytuple[0] == 'exit'):
										sys.exit(0)
									else:
										print colored("[!] Unknown command", "red")
							elif(usefuzzer2_1 == '3'):
								break
							else:
								print colored("[!] Unknown option", "red")
					elif(usefuzzer == '3'):
						print colored("[1] Browser", "blue")
						print colored("[2] OS", "blue")
						print colored("[3] back", "blue")
						while True:
							usefuzzer2_2 = raw_input("[haxxor/fuzzers/linux] => ")
							if(usefuzzer2_2 == '1'):
								call("ls -1 /usr/haxxor/fuzzers/linux/browser", shell=True)
								while True:
									usefuzzer2_2_1 = raw_input("[haxxor/fuzzers/linux/Browser] => ")
									mytuple3_1 = usefuzzer2_2_1.partition(" ")
									if(mytuple3_1[0] == 'use'):
										call("python " + mytuple3_1[2], shell=True)
									elif(mytuple[0] == 'back'):
										break
									elif(mytuple[0] == 'exit'):
										sys.exit(0)
									else:
										print colored("[!] Unknown command", "red")
							elif(usefuzzer2_2 == '2'):
								call("ls -1 /usr/haxxor/fuzzers/linux/os", shell=True)
								while True:
									usefuzzer2_2_2 = raw_input("[haxxor/fuzzers/linux/OS] => ")
									mytuple3_2 = usefuzzer2_2_2.partition(" ")
									if(mytuple3_2[0] == 'use'):
										call("python " + mytuple3_2[2], shell=True)
									elif(mytuple3_2[0] == 'back'):
										break
									elif(mytuple3_2[0] == 'exit'):
										sys.exit(0)
									else:
										print colored("[!] Unknown command", "red")
							elif(usefuzzer2_2 == '3'):
								break
							else:
								print colored("[!] Unknown option", "red")
					elif(usefuzzer == '4'):
						print colored("[1] Browser", "blue")
						print colored("[2] OS", "blue")
						print colored("[3] back", "blue")
						while True:
							usefuzzer2_3 = raw_input("[haxxor/fuzzers/misc] => ")
							if(usefuzzer2_3 == '1'):
								call("ls -1 /usr/haxxor/fuzzers/misc/browser", shell=True)
								while True:
									usefuzzer2_3_1 = raw_input("[haxxor/fuzzers/misc/Browser] => ")
									mytuple4_1 = usefuzzer2_3_1.partition(" ")
									if(mytuple4_1[0] == 'use'):
										call("python " + mytuple4_1[2], shell=True)
									elif(mytuple4_1[0] == 'back'):
										break
									elif(mytuple4_1[0] == 'exit'):
										sys.exit(0)
									else:
										print colored("[!] Unknown option", "red")
							elif(usefuzzer2_3 == '2'):
								call("ls -1 /usr/haxxor/fuzzers/misc/os", shell=True)
								while True:
									usefuzzer2_3_2 = raw_input("[haxxor/fuzzers/misc/OS] => ")
									mytuple4_2 = usefuzzer2_3_2.partition(" ")
									if(mytuple4_2[0] == 'use'):
										call("python " + mytuple4_2[2], shell=True)
									elif(mytuple4_2[0] == 'back'):
										break
									elif(mytuple4_2[0] == 'exit'):
										sys.exit(0)
									else:
										print colored("[!] Unknown command", "red")
							elif(usefuzzer2_3 == '3'):
								break
							else:
								print colored("[!] Unknown command", "red")
					elif(usefuzzer == '5'):
						break
					else:
						print colored("[!] Unknown option", "red")
			except KeyboardInterrupt:
				print colored("[!] #5 to go back", "red")
	except KeyboardInterrupt:
		print colored("[!] Error", "red")
	
	def mainmenu():
		try:
			first_option = raw_input("[haxxor] => ")
			if(first_option == '1'):
				fuzzers()
			elif(first_option == '2'):	
				print colored("[!] Not done yet", "red")
			elif(first_option == '3'):
				print colored("[!] Not done", "red")
			elif(first_option == '4'):
				print colored("[!] Not done", "red")
			elif(first_option == '5'):
				print colored("[====================================]", "yellow")
				print colored("[1 - 4: different tools              ]", "yellow")
				print colored("[5: this menu                        ]", "yellow")
				print colored("[6: donate to the project            ]", "yellow")
				print colored("[7: exit                             ]", "yellow")
				print colored("[====================================]", "yellow")
			elif(first_option == '6'):
				pass
			elif(first_option == '7'):
				sys.exit(0)
			else:
				print colored("[!] Unknown option", "red")
		except KeyboardInterrupt:
			print colored("[!] Option #7 to exit", "red")
	mainmenu()
while True:
	main()
