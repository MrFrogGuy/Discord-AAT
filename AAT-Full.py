LICENSE = """
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.
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
l_args = [
	[colorama.Fore.RED, colorama.Fore.RESET],
	[colorama.Fore.GREEN, colorama.Fore.RESET],
	[colorama.Fore.YELLOW, colorama.Fore.RESET]
]
aatPrefix = "aat "

is_self = lambda msg: True if msg.author == aatClient.user else False
aerror = lambda msg: print("{}Error\t{}{}] {}".format(*l_args[0], time.strftime("%H:%M:%S"), msg))
ainfo = lambda msg: print("{}Info\t{}{}] {}".format(*l_args[1], time.strftime("%H:%M:%S"), msg))
awarning = lambda msg: print("{}Warning\t{}{}] {}".format(*l_args[2], time.strftime("%H:%M:%S"), msg))

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
		
@aatClient.event
async def on_message(mesg: discord.Message) -> None:
	if is_self(mesg) and mesg.content.startswith(aatPrefix):
		arguments = mesg.content.strip(aatPrefix).split()
		params = [None] # Limit, *
		if arguments[0] in ["purge", "delete"]:
			if "-d" in arguments:
				pass
