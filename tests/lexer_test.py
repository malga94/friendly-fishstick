import pytest

from lexer import lexer
from config.constants import CREATE, SELECT, FROM, WHERE 

create_table_inputs = [('''CreAtE TABle pasta
                   	( shape string, sauce
        		string)''', {'name':'pasta', 'cols':{'shape':'string', 'sauce':'string'}}),
		       ('''CREATE TABLE pizza (kind string,
			 toppings_no int, toppings string)''', 
			{'name': 'pizza', 'cols':{'kind':'string', 'toppings_no':'int', 'toppings':'string'}})]

@pytest.mark.parametrize("query,result", create_table_inputs)
def test_create_table(query, result):
	
	type, name, cols = lexer(query)
	assert type == CREATE
	assert name == result['name']
	assert cols == result['cols']
