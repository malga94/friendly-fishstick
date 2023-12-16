import re
from typing import Callable
from config.constants import CREATE, SELECT, FROM, WHERE, TYPES, SCHEMA, INVALID

def lexer(command: str) -> str:
	command = command.strip()
	if ' '.join(command.split(' ')[:2]).upper() == CREATE:
		tname, columns = handle_create(command)
		return CREATE, tname, columns		

	if command[:6].upper() == SELECT:
		tname, filters = handle_select(command)
		return SELECT, tname, filters

	if command[:6].upper() == SCHEMA:
		tnames = handle_schema(command)
		return SCHEMA, tnames

	else:
		return INVALID, None, None

def handle_create(command: str) -> tuple[str, str, list[str]]:
	
	name_pattern = r'(\w* ){2}(\w*)'
	try:
		tname = re.search(name_pattern, command).group(2)
	except AttributeError:
		print("Invalid syntax: must provide table name")
		return None, None
	
	pattern = r'\(([\s]*[a-z][^,]*,)*([\s]*[a-z][^,]*)'
	try:
		columns = re.search(pattern, command).group().replace('(','').replace(')','').replace('\n','')
	except AttributeError:
		print("Invalid syntax: must provide at least one column")
		return None, None
	columns = ' '.join(columns.split()) #Replace multiple whitespace with single whitespace
	schema = {}
	
	for col in columns.split(','):
		
		name, type = col.strip().split(' ')
		if type not in TYPES.keys():
			print(f"Invalid type {type}")
			return None, None
		schema[name] = type
	
	return tname, schema	

def handle_select(command: str) -> tuple[str, str, list[str]]:
	pass 

def handle_schema(command: str) -> tuple[str, list[str]]:
	tnames = [name.strip() for name in command.split(' ')[1:]]
	return tnames
