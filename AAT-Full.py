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
	import aat_utils
	import os, sys
except ImportError as Error:
	print(f"ERROR     ]: Missing module: {Error.name}")
	exit(1)

# If error with import:
"""
conda install discord  || python3 -m pip install discord  || pip install discord
conda install colorama || python3 -m pip install colorama || pip install colorama
# If aat_arguments is missing: 

 if [ -d aat_utils ]; then
	 wget https://raw.githubusercontent.com/MrFrogGuy/Discord-AAT/main/aat_arguments.py -O \
 	aat_utils/aat_arguments.py
else
	mkdir aat_utils ; wget https://raw.githubusercontent.com/MrFrogGuy/Discord-AAT/main/aat_arguments.py -O \
 	aat_utils/aat_arguments.py
fi
"""
aatClient = discord.Client()

def write_log(fname: str, logs: list, append=False, overwrite=True) -> bool:
	if os.path.isfile(fname):
		try:
			descriptor = open(fname, "w") if overwrite and not append Else open(fname, "a")
			descriptor.writelines(logs)
			aat_utils.args.ainfo(f"Appended logs to: {fname}")
		except Exception as Error:
			aerror(f)
	else:
		descriptor = open(fname, "w")
		descriptor.writelines(logs)
		aat_utils.args.ainfo(f"Wrote logs to: {fname}")
		
# No error returns, if you want error returns... Refer to aat_utils/misc.py
# Copy the code for each error and place it here.
# What I mean by this is: replying with an error embed &/ message when you've..
# .... done something wrong or a command has failed to do its set task.

@aatClient.event
async def on_message(mesg: discord.Message) -> None:
	if is_self(mesg) and mesg.content.startswith(aatPrefix):
		arguments = mesg.content.strip(aatPrefix).split()
		if arguments[0] in ["log", "save_chat"]:
			coarg0, coarg1 = [aat_utils.args.cmd_arguments["writelog"],
				aat_utils.args.cmd_arguments["chistory"]
			]
			log_list = []
			if "-l" in arguments and aat_utils.args.has_args(arguments, "-l"):
				data  = argfor(arguments, "-l")
				if data.isdigit():
					coarg1["limit"] = int(argfor(data))
				else:
					return
			if "-o" in arguments and aat_utils.args.has_args(arguments, "-o"):
				coarg0["fname"] = argfor(arguments, "-o")
			if coarg0['fname'] == "logs.log":
				coarg0 = f"{str(mesg.channel)}-{time.strftime(aat_utils.args.aatLFormat)}"
			async for message in mesg.channel.history(*coarg1):
				log_list.append("[{} | {}]: {}".format(
					message.creation_date,
					message.author, message.content
				) if message.content not in (None, "") else "[{} | {}]: {}".format(
					message.creation_date,
					message.author, message.type))
			write_logs(**coarg0)
		if arguments[0] == "purge":
			limit = None
			coarg0 = aat_utils.args.cmd_arguments["chistory"]
			if "-l" in arguments and aat_utils.args.has_args(arguments, "-l"):
				if aat_utils.args.argfor(arguments, "-l").isdigit():
					coarg["limit"] = aat_utils.args.argfor(arguments, "-l")
			try:
				async for message in mesg.channel.history(**coarg1):
					if is_self(message):
						await message.delete()
			except:
				pass
