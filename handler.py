from dataclasses import dataclass, make_dataclass, field
from config.constants import TYPES
from typing import Any

from config.constants import CREATE, SELECT, FROM, WHERE, TYPES, INVALID
from lexer import lexer

@dataclass
class Relation:
	
	name: str
	schema: dict
	rows: list[Any] = field(default_factory=list)

def handle_user_input(db: dict, user_input: str) -> dict:

	command_type, r1, r2 = lexer(user_input)
	if command_type == CREATE:
		name = r1
		attributes = r2
		
		table = Relation(name, attributes)
		db[name] = table
		return db
	
	elif command_type == INVALID:
		print(f"Invalid command {user_input}")
		return db
	else:
		raise NotImplementedError(f"Command {command_type} not implemented yet")
