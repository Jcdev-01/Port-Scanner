#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py")

#Add a pretty banner

print("""
     _      ____                   ___  _ 
    | | ___|  _ \  _____   __     / _ \/ |
 _  | |/ __| | | |/ _ \ \ / /____| | | | |
| |_| | (__| |_| |  __/\ V /_____| |_| | |
 \___/ \___|____/ \___| \_/       \___/|_|
                                          
 OPEN-SOURCE PROJECT | https://github.com/Jcdev-01/Port-Scanner

                Port Scanner by JcDev-01

    """);
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(20,443):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator - if port is open it throws a 0, otherwise 1
		if result == 0:
			print(f"Port {port} is open")
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()