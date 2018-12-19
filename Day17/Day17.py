import sys
import string
import numpy as np

def Import_Data(path):
	f = open(path, 'r')
	return f.read().strip().split('\n')

def Generate_Grid(strings):
	arr = np.zeros((15,20))
	for line in strings:
		if line[0] == 'x':
			x = int(line.split('=')[1].split(',')[0])
			ymin = int(line.split('=')[2].split('..')[0])
			ymax = int(line.split('=')[2].split('..')[1])
			arr[ymin:ymax + 1,x] = 2
		elif line[0] == 'y':
			y = int(line.split('=')[1].split(',')[0])
			xmin = int(line.split('=')[2].split('..')[0])
			xmax = int(line.split('=')[2].split('..')[1])
			arr[y, xmin:xmax + 1] = 2
		else:
			print('error')
	return arr

def Simulate(grid, ticks):
	for i in range(0, len(ticks)):
		


def main():
	path = sys.argv[1]
	data = Import_Data(path)
	grid = Generate_Grid(data)

	print(grid)
	

if __name__ == '__main__':
	main()
	exit(0)