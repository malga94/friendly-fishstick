from dataclasses import dataclass, make_dataclass, field
from config.constants import TYPES
from typing import Any

from config.constants import CREATE, SELECT, FROM, WHERE, TYPES, SCHEMA, INVALID
from lexer import lexer

@dataclass
class Relation:
	
	name: str
	schema: dict
	rows: list[Any] = field(default_factory=list)

def handle_user_input(db: dict, user_input: str) -> dict:

	command_type, *r = lexer(user_input)
	if command_type == CREATE:
		name = r[0]
		attributes = r[1]
		
		if name:	
			table = Relation(name, attributes)
			db[name] = table
	
	elif command_type == SCHEMA:
		names = r[0]
		for name in names:
			table = db.get(name)
			if table:
				schema = table.schema
				print(f"{name} {schema=}")
			else:
				print(f"Table named {name} does not exist")
		
	elif command_type == INVALID:
		print(f"Invalid command {user_input}")
	
	else:
		raise NotImplementedError(f"Command {command_type} not implemented yet")

	return db
