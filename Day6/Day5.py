import sys
import string

def Import_Data(path):
	f = open(path, 'r')
	return f.read().strip()

def main():
	path = sys.argv[1]
	data = Import_Data(path)
	

if __name__ == '__main__':
	main()
	exit(0)