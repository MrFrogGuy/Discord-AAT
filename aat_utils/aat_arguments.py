from colorama import Fore as fg
from time import strftime

l_args = [
	[fg.RED, fg.RESET],
	[fg.GREEN, fg.RESET],
	[fg.YELLOW, fg.RESET]
] # For the colorama arguments

aatPrefix = "aat "  #Bot command prefix Example: aat purge [*args]


is_self = lambda msg: True if msg.author == aatClient.user else False
aerror = lambda msg: print("{}Error\t{}{}] {}".format(*l_args[0], strftime("%H:%M:%S"), msg))
ainfo = lambda msg: print("{}Info\t{}{}] {}".format(*l_args[1], strftime("%H:%M:%S"), msg))
awarning = lambda msg: print("{}Warning\t{}{}] {}".format(*l_args[2], strftime("%H:%M:%S"), msg))


purge_arguments = {
	"to_pass": [
		None, # Limit
		None, # Before (UTC ex: 1-1-2020)
		None, # After (UTC ex: 1-1-2020)
		None, # Around (UTC ex: 1-1-2020)
		False # Oldest first | If set to True, return messages in oldest->newest order.
	]
}