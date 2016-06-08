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
wd = commands.getoutput("pwd")
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
scanner1 = int(commands.getoutput("ls -1 /usr/haxxor/scanners/version |wc -l"))
scanner2 = int(commands.getoutput("ls -1 /usr/haxxor/scanners/os |wc -l"))
scanner3 = int(commands.getoutput("ls -1 /usr/haxxor/scanners/kernel |wc -l"))
scanner4 = int(commands.getoutput("ls -1 /usr/haxxor/scanners/software |wc -l"))
list_scanners = int(scanner1 + scanner2 + scanner3 + scanner4)
privescs1 = int(commands.getoutput("ls -1 /usr/haxxor/privesc/windows |wc -l"))
privescs2 = int(commands.getoutput("ls -1 /usr/haxxor/privesc/mac |wc -l"))
privescs3 = int(commands.getoutput("ls -1 /usr/haxxor/privesc/linux |wc -l"))
privescs4 = int(commands.getoutput("ls -1 /usr/haxxor/privesc/misc |wc -l"))
list_privesc = int(privescs1 + privescs2 + privescs3 + privescs4)
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
	print colored("[1] fuzzers", "blue")
	print colored("[2] modules", "blue")
	print colored("[3] scanners", "blue")
	print colored("[4] privesc", "blue")
	print colored("[5] help", "blue")
	print colored("[6] donate", "blue")
	print colored("[7] exit", "blue")
banner()

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
										print colored("[1] Browser", "blue")
										print colored("[2] OS", "blue")
										print colored("[3] back", "blue")
										break
									elif(mytuple1_1[0] == 'exit'):
										sys.exit(0)
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
									elif(mytuple1_2[0] == 'back'):
										print colored("[1] Browser", "blue")
										print colored("[2] OS", "blue")
										print colored("[3] back", "blue")
										break
									else:
										print colored("[!] Unknown option", "red")	
							elif(usefuzzer1 == '3'):
								print colored("[1] Windows\n[2] Mac\n[3] Linux\n[4] Misc\n[5] back", "blue")
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
										print colored("[1] Browser\n[2] OS\n[3] back", "blue")
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
										print colored("[1] Browser\n[2] OS\n[3] back", "blue")
										break
									elif(mytuple[0] == 'exit'):
										sys.exit(0)
									else:
										print colored("[!] Unknown command", "red")
							elif(usefuzzer2_1 == '3'):
								print colored("[1] Windows\n[2] Mac\n[3] Linux\n[4] Misc\n[5] back", "blue")
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
									elif(mytuple3_1[0] == 'back'):
										print colored("[1] Browser\n[2] OS\n[3] back", "blue")
										break
									elif(mytuple3_1[0] == 'exit'):
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
										print colored("[1] Browser\n[2] OS\n[3] back", "blue")
										break
									elif(mytuple3_2[0] == 'exit'):
										sys.exit(0)
									else:
										print colored("[!] Unknown command", "red")
							elif(usefuzzer2_2 == '3'):
								print colored("[1] Windows\n[2] Mac\n[3] Linux\n[4] Misc\n[5] back", "blue")
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
										print colored("[1] Browser\n[2] OS\n[3] back", "blue")
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
										print colored("[1] Browser\n[2] OS\n[3] Back", "blue")
										break
									elif(mytuple4_2[0] == 'exit'):
										sys.exit(0)
									else:
										print colored("[!] Unknown command", "red")
							elif(usefuzzer2_3 == '3'):
								print colored("[1] Windows\n[2] Mac\n[3] Linux\n[4] Misc\n[5] back", "blue")
								break
							else:
								print colored("[!] Unknown command", "red")
					elif(usefuzzer == '5'):
						call("clear", shell=True)
						banner()
						break
					else:
						print colored("[!] Unknown option", "red")
			except KeyboardInterrupt:
				print colored("[!] #5 to go back", "red")
	except KeyboardInterrupt:
		print colored("[!] Error", "red")
	def modules():
		try:
			print colored("[1] DNS\n[2] Enumeration\n[3] Scanning\n[4] back", "blue")
			while True:
				usemodule1 = raw_input("[haxxor/modules] => ")
				if(usemodule1 == '1'):
					call("ls -1 /usr/haxxor/modules/dns", shell=True)
					while True:
						usefuzzer1_1 = raw_input("[haxxor/modules/dns] => ")
						module_tuple1 = usefuzzer1_1.partition(" ")
						if(module_tuple1[0] == 'use'):
							call("python /usr/haxxor/modules/dns/" + module_tuple1[2], shell=True)
						elif(module_tuple1[0] == 'back'):
							print colored("[1] DNS\n[2] Enumeration\n[3] Scanning\n[4] back", "blue")
							break
						elif(module_tuple1[0] == 'exit'):
							sys.exit(0)
						else:
							print colored("[!] Unknown command", "red")
				elif(usemodule1 == '2'):
					call("ls -1 /usr/haxxor/modules/enumeration", shell=True)
					while True:
						usemodule1_2 = raw_input("[haxxor/modules/enum] => ")
						module_tuple2 = usemodule1_2.partition(" ")
						if(module_tuple2[0] == 'use'):
							call("python /usr/haxxor/modules/enumeration/" + module_tuple2[2], shell=True)
						elif(module_tuple2[0] == 'back'):
							print colored("[1] DNS\n[2] Enumeration\n[3] Scanning\n[4] back")
							break
						elif(module_tuple2[0] == 'exit'):
							sys.exit(0)
						else:
							print colored("[!] Unknown command", "red")
				elif(usemodule1 == '3'):
					call("ls -1 /usr/haxxor/modules/scanning", shell=True)
					while True:
						usemodule1_3 = raw_input("[haxxor/modules/scanning] => ")
						module_tuple3 = usemodule1_3.partition(" ")
						if(module_tuple3[0] == 'use'):
							call("python /usr/haxxor/modules/scanning/" + module_tuple3[2], shell=True)
						elif(module_tuple3[0] == 'back'):
							print colored("[1] DNS\n[2] Enumeration\n[3] Scanning\n[4] back", "blue")
							break
						elif(module_tuple3[0] == 'exit'):
							sys.exit(0)
						else:
							print colored("[!] Unknown command", "red")
				elif(usemodule1 == '4'):
					call("clear", shell=True)
					banner()
					break
				else:
					print colored("[!] Unknown option", "red")
		except KeyboardInterrupt:
			print colored("[!] Option #4 to go back", "red")
	def scanners():
		try:
			print colored("[1] Version\n[2] OS\n[3] Kernel\n[4] Software\n[5] back", "blue")
			while True:
				usescanner1 = raw_input("[haxxor/scanners] => ")
				if(usescanner1 == '1'):
					call("ls -1 /usr/haxxor/scanners/version", shell=True)
					while True:
						scanner1 = raw_input("[haxxor/scanners/version] => ")
						scanner_tuple1 = scanner1.partition(" ")
						if(scanner_tuple1[0] == 'use' or scanner_tuple1[1] == 'use'):
							call("python /usr/haxxor/scanners/version/" + scanner_tuple1[2], shell=True)	
						elif(scanner_tuple1[0] == 'back'):
							print colored("[1] Version\n[2] OS\n[3] Kernel\n[4] Software\n[5] back", "blue")
							break
						elif(scanner_tuple1[0] == 'exit'):
							sys.exit(0)
						else:
							print colored("[!] Unknown command", "red")
				elif(usescanner1 == '2'):
					call("ls -1 /usr/haxxor/scanner/os", shell=True)
					while True:
						scanner2 = raw_input("[haxxor/scanners/os] => ")
						scanner_tuple2 = scanner2.partition(" ")
						if(scanner_tuple2[0] == 'use'):
							call("python /usr/haxxor/scanners/os/" + scanner_tuple2[2], shell=True)
						elif(scanner_tuple2[0] == 'back'):
							print colored("[1] Version\n[2] OS\n[3] Kernel\n[4] Software\n[5] back", "blue")
							break
						elif(scanner_tuple2[0] == 'exit'):
							sys.exit(0)
						else:
							print colored("[!] Unknown commnand", "red")
				elif(usescanner1 == '3'):
					call("ls -1 /usr/haxxor/scanners/kernel", shell=True)
					while True:
						scanner3 = raw_input("[haxxor/scanners/kernel] => ")
						scanner_tuple3 = scanner3.partition(" ")
						if(scanner_tuple3[0] == 'use'):
							call("python /usr/haxxor/scanners/kernel/" + scanner_tuple3[2], shell=True)
						elif(scanner_tuple3[0] == 'back'):
							print colored("[1] Version\n[2] OS\n[3] Kernel\n[4] Software\n[5] back", "blue")
							break
						elif(scanner_tuple3[0] == 'exit'):
							sys.exit(0)
						else:
							print colored("[!] Unknown command", "red")
				elif(usescanner1 == '4'):
					call("ls -1 /usr/haxxor/scanners/software", shell=True)
					while True:
						scanner4 = raw_input("[haxxor/scanners/spftware] => ")
						scanner_tuple4 = scanner4.partition(" ")
						if(scanner_tuple4[0] == 'use'):
							call("python /usr/haxxor/scanners/software/" + scanner_tuple4[2], shell=True)
						elif(scanner_tuple4[0] == 'back'):
							print colored("[1] Version\n[2] OS\n[3] Kernel\n[4] Software\n[5] back", "blue")
							break
						elif(scanner_tuple4[0] == 'exit'):
							sys.exit(0)
						else:
							print colored("[!] Unknown command", "red")
				elif(usescanner1 == '5'):
					call("clear", shell=True)
					banner()
					break
				else:
					print colored("[!] Unknown option", "red")

		except KeyboardInterrupt:
			print colored("[!] Option #5 to go back to menu", "red")
	def privesc():
		try:
			print colored("[1] Windows\n[2] Mac\n[3] Linux\n[4] Misc\n[5] back", "blue")
			while True:
				useprivesc1 = raw_input("[haxxor/privesc] => ")
				if(useprivesc1 == '1'):
					call("ls -1 /usr/haxxor/privesc/windows", shell=True)
					while True:
						privesc1 = raw_input("[haxxor/privesc/windows] => ")
						privesc_tuple1 = privesc1.partition(" ")
						if(privesc_tuple1[0] == 'use'):
							call("python /usr/haxxor/privesc/windows/" + privesc_tuple1, shell=True)
						elif(privesc_tuple1[0] == 'back'):
							print colored("[1] Windows\n[2] Mac\n[3] Linux\n[4] Misc\n[5] back", "blue")
							break
						elif(privesc_tuple1[0] == 'exit'):
							sys.exit(0)
						elif(privesc_tuple1[0] == 'help'):
							print colored("[=================================================]", "yellow")
							print colored("[help: this menu                                  ]", "yellow")
							print colored("[back: go back to previous menu                   ]", "yellow")
							print colored("[exit: exit haxxor-framework                      ]", "yellow")
							print colored("[use: use script                                  ]", "yellow")
							print colored("[=================================================]", "yellow")
						else:
							print colored("[!] Unknown command", "red")
				elif(useprivesc1 == '2'):
					call("ls -1 /usr/haxxor/privesc/mac", shell=True)
					while True:
						privesc2 = raw_input("[haxxor/privesc/mac] => ")
						privesc_tuple2 = privesc2.partition(" ")
						if(privesc_tuple2[0] == 'use'):
							call("python /usr/haxxor/privesc/mac/" + privesc_tuple2[2], shell=True)
						elif(privesc_tuple2[0] == 'back'):
							print colored("[1] Windows\n[2] Mac\n[3] Linux\n[4] Misc\n[5] back", "blue")
							break
						elif(privesc_tuple2[0] == 'exit'):
							sys.exit(0)
						elif(privesc_tuple2[0] == 'help'):
							print colored("[=================================================]", "yellow")
                                                        print colored("[help: this menu                                  ]", "yellow")
                                                        print colored("[back: go back to previous menu                   ]", "yellow")
                                                        print colored("[exit: exit haxxor-framework                      ]", "yellow")
                                                        print colored("[use: use script                                  ]", "yellow") 
                                                        print colored("[=================================================]", "yellow")
						else:
							print colored("[!] Unknown command", "red")
				elif(useprivesc1 == '3'):
					call("ls -1 /usr/haxxor/privesc/linux", shell=True)
					while True:
						privesc3 = raw_input("[haxxor/privesc/linux] => ")
						privesc_tuple3 = privesc3.partition(" ")
						if(privesc_tuple3[0] == 'use'):
							call("python /usr/haxxor/privesc/linux/" + privesc_tuple3[0], shell=True)
						elif(privesc_tuple3[0] == 'back'):
							print colored("[1] Windows\n[2] Mac\n[3] Linux\n[4] Misc\n[5] Misc", "blue")
						elif(privesc_tuple3[0] == 'exit'):
							sys.exit(0)
						elif(privesc_tuple3[0] == 'help'):
							print colored("[=================================================]", "yellow")
                                                        print colored("[help: this menu                                  ]", "yellow")
                                                        print colored("[back: go back to previous menu                   ]", "yellow")
                                                        print colored("[exit: exit haxxor-framework                      ]", "yellow")
                                                        print colored("[use: use script                                  ]", "yellow") 
                                                        print colored("[=================================================]", "yellow")
						else:
							print colored("[!] Unknown command", "red")
				elif(useprivesc1 == '4'):
					call("ls -1 /usr/haxxor/privesc/misc", shell=True)
					while True:
						privesc4 = raw_input("[haxxor/privesc/misc] => ")
						privesc_tuple4 = privesc4.partition(" ")
						if(privesc_tuple4[0] == 'use'):
							call("python /usr/haxxor/privesc/misc/" + privesc_tuple4, shell=True)
						elif(privesc_tuple4[0] == 'back'):
							print colored("[1] Windows\n[2] Mac\n[3] Linux\n[4] Misc\n[5] back", "blue")
							break
						elif(privesc_tuple4[0] == 'exit'):
							sys.exit(0)
						elif(privesc_tuple4[0] == 'help'):
							print colored("[=================================================]", "yellow")
                                                        print colored("[help: this menu                                  ]", "yellow")
                                                        print colored("[back: go back to previous menu                   ]", "yellow")
                                                        print colored("[exit: exit haxxor-framework                      ]", "yellow")
                                                        print colored("[use: use script                                  ]", "yellow") 
                                                        print colored("[=================================================]", "yellow")
						else:
							print colored("[!] Unknown command", "red")
				elif(privesc1 == '5'):
					call("clear", shell=True)
					banner()
					break
				else:
					print colored("[!] Unknown option", "red")
		except KeyboardInterrupt:
			print colored("[!] Option #5 to go back", "red")	 
	def mainmenu():
		try:
			first_option = raw_input("[haxxor] => ")
			if(first_option == '1'):
				fuzzers()
			elif(first_option == '2'):	
				modules()
			elif(first_option == '3'):
				scanners()
			elif(first_option == '4'):
				privesc()
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
