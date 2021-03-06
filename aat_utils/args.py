from colorama import Fore as fg
from time import strftime

l_args = [
	[fg.RED, fg.RESET],
	[fg.GREEN, fg.RESET],
	[fg.YELLOW, fg.RESET]
] # For the colorama arguments

aatTFormat = "%H:%M:%S"
aatLFormat = "%H:%M:%S-%d-%m-%y.log"
aatPrefix = "aat "  #Bot command prefix Example: aat purge [*args]


is_self = lambda msg: True if msg.author == aatClient.user else False
arg_for = lambda lst, data: lst[lst.index(data) + 1]
has_args = lambda lst, data: True if ( len(lst) > lst.index(data) + 1 ) else False
aerror = lambda msg: print("{}Error\t{}{}] {}".format(*l_args[0], strftime(aatTFormat), msg))
ainfo = lambda msg: print("{}Info\t{}{}] {}".format(*l_args[1], strftime(aatTFormat), msg))
awarning = lambda msg: print("{}Warning\t{}{}] {}".format(*l_args[2], strftime(aatTFormat), msg))

if not os.path.isdir('Chat-Logs'): os.mkdir('Chat-Logs')
if not os.path.isdir('Delete-Logs'): os.mkdir('Delete-Logs')
ainfo("Log paths set.")

# While you may question why I'm using dict's, just keep in mind:
# They're needed for positional arguments -> **

cmd_arguments = {
	"chistory": {
		"limit":None, # Limit
		"before":None, # Before (UTC ex: 1-1-2020)
		"after":None, # After (UTC ex: 1-1-2020)
		"around":None, # Around (UTC ex: 1-1-2020)
		"oldest_first": True
	}, # Oldest first | If set to True, return messages in oldest->newest order.
	"log-down": [
		None, # Limit
		"Chat-Logs/chat.log"], # Directory/file,
	"writelog": {
		"fname": "logs.log",
		"logs": [],
		"append": False,
		"overwrite": True
	}
}

ainfo("Argument library fully imported.")
