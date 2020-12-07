LICENSE = """                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
 """

# Imports
try:
	import discord
	import time
	import colorama
	import os, sys
except ImportError as Error:
	print(f"ERROR     ]: Missing module: {Error.name}")
	exit(1)

# If error with import:
	# conda install discord  || python3 -m pip install discord  || pip install discord
	# conda install colorama || python3 -m pip install colorama || pip install colorama

aatClient = discord.Client() 
ismines = lambda msg: True if msg.author == aatClient.user else False

args = [
	[colorama.Fore.RED, colorama.Fore.RESET],
	[colorama.Fore.GREEN, colorama.Fore.RESET],
	[colorama.Fore.YELLOW, colorama.Fore.RESET]
]

aerror = lambda msg: print("{}Error\t{}{}] {}".format(*args[0], time.strftime("%H:%M:%S"), msg))
ainfo = lambda msg: print("{}Info\t{}{}] {}".format(*args[1], time.strftime("%H:%M:%S"), msg))
awarning = lambda msg: print("{}Warning\t{}{}] {}".format(*args[2], time.strftime("%H:%M:%S"), msg))

def write_log(fname: str, logs: list, append=False, overwrite=True) -> bool:
	if os.path.isfile(fname):
		try:
			descriptor = open(fname, "w") if overwrite and not append Else open(fname, "a")
			descriptor.writelines(logs)
			ainfo(f"Appended logs to: {fname}")
		except Exception as Error:
			aerror(f)
	else:
		descriptor = open(fname, "w")
		descriptor.writelines(logs)
		ainfo(f"Wrote logs to: {fname}")
