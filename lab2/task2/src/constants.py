import re

HELP_INFO = 'Available commands: help - switch - add - remove - find - list - grep - save - load - exit\nEnter command name and pass parameters (between "text1 text2" if you want to group them).\nswitch <username> -> switches to user or creates if does not exist\nadd [params] -> add params to current user storage\nremove <param> -> remove param from current user storage\nfind [params] -> prints all found params or message that there are no such params\nlist -> prints current user storage\ngrep <pattern> -> search for items in storage that match a pattern\nexit -> quit program'

COMMAND_PATTERN = re.compile(
    r'(?<!\S)\b(?:add|remove|find|grep|save|load|list|switch|help|exit)\b(?=(?:(?:[^"]*"){2})*[^"]*$)(?<!")')

ARGS_PATTERN = re.compile(r'("[^"]+"|\S+)')
