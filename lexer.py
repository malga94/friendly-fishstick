import re
from config.constants import CREATE, SELECT, FROM, WHERE, TYPES, INVALID

def lexer(command: str) -> str:
	command = command.strip()
	if ' '.join(command.split(' ')[:2]).upper() == CREATE:
		tname, columns = handle_create(command)
		return CREATE, tname, columns		

	if command[:6].upper() == SELECT:
		tname, filters = handle_select(command)
		return SELECT, tname, filters

	else:
		return INVALID, None, None

def handle_create(command: str) -> tuple[str, str, list[str]]:
	
	name_pattern = r'(\w* ){2}(\w*)'
	tname = re.search(name_pattern, command).group(2)
	
	pattern = r'\(([\s]*[a-z][^,]*,)*([\s]*[a-z][^,]*)'
	columns = re.search(pattern, command).group().replace('(','').replace(')','').replace('\n','')
	columns = ' '.join(columns.split()) #Replace multiple whitespace with single whitespace
	schema = {}
	
	for col in columns.split(','):
		
		name, type = col.strip().split(' ')
		if type not in TYPES.keys():
			raise TypeError(f'Invalid type {type}')
		schema[name] = type
	
	return tname, schema	

def handle_select(command: str) -> tuple[str, str, list[str]]:
	pass 

