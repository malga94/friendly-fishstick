import argparse

from handler import handle_user_input

def main():
	
	parser = argparse.ArgumentParser()
	parser.add_argument('db', type=str, nargs='?')
	
	args = parser.parse_args()
	print("Welcome to SqlShit\u2122!")
	
	if args.db:
		with open(f'db/{args.db}', 'r') as f:
			data = f.read()
			
		print(f"Using database {args.db}")	

	else:
		print("Using temporary in-memory database")
		db = {}
	
	user_input = ''
	while True:
		print('>>> ', end='')
		user_input = input()
		
		if user_input.lower() == 'quit':
			break
		
		if user_input.lower() == 'tables':
			print(f"{[name for name in db.keys()]}")
		
		else:
			db = handle_user_input(db, user_input)				


if __name__ == '__main__':
	main()
	
