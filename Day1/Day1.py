import sys

def Import_Data(path):
	f = open(path, 'r')
	return f.read().split('\n')

def main():
	path = sys.argv[1]
	data = Import_Data(path)
	lastFreqs = []
	counter = 0
	freq = 0
	while(True):
		for line in data:
			freq += int(line)
			if freq in lastFreqs:
				print(freq)
				return
			lastFreqs.append(freq)

			print(counter)
			counter += 1
	return

if __name__ == '__main__':
	main()
	exit(0)