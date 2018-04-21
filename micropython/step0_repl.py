from sys import stdin

def READ( input ):
	return input

def EVAL( input ):
	return input

def PRINT( input ):
	return input

def rep( input):
	return (PRINT(EVAL(READ(input))))

def main():
	while True:
		try:
			line = input ("user> ")
			print(rep(line))
		except EOFError:
			print("\nQuitting...")
			break

if __name__ == "__main__":
    main()
