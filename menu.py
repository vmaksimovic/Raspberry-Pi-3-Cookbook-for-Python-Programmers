#!/usr/bin/python3
#menu.py
from subprocess import call

filename="menu.ini"
DESC=0
KEY=1
CMD=2

print("Strat menu")
try:
	with open(filename) as f:
		menufile = f.readlines()
except IOError:
	print("Unable to open %s"%(filename))
for item in menufile:
	line = item.split(',')
	print("(%s): %s" %(line[KEY],line[DESC]))

#Get user input

running = True

while(running):
	user_input = raw_input()
	#chech input, and execute command
	for item in menufile:
		line = item.split(',')
		if (user_input == line[KEY]):
			print("Command : " +line[KEY])
			#call the script
			#e.g. call(["ls", "-1"])
			commands = line[CMD].rstrip().split()
			print(commands)
			running= False
			#only run command is one if available
			if len(commands):
				call(commands)
	if (running==True):
		print("key not found!")
print("All done!")
#END
