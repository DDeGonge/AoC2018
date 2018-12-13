import sys
import string
import numpy as np

# ORIENTATIONS
# 0: up
# 1: right
# 2: down
# 3: left

np.set_printoptions(threshold=np.inf)

def Import_Data(path):
	f = open(path, 'r')
	return f.read().split('\n')

def Find_Carts(ingrid):
	newgrid = [list(ingrid[x]) for x in range(0, len(ingrid))]
	print(newgrid)
	carts = []
	for y, line in enumerate(newgrid):
		print(line)
		for x, ch in enumerate(line):
			print(x,y)
			if ch == '^':
				carts.append((x,y,0))
				newgrid[x][y] = '|'
			elif ch == '>':
				carts.append((x,y,1))
				newgrid[x][y] = '-'
			elif ch == 'v':
				carts.append((x,y,2))
				newgrid[x][y] = '|'
			elif ch == '<':
				carts.append((x,y,3))
				newgrid[x][y] = '-'


	return carts, newgrid

def main():
	path = sys.argv[1]
	inputs = Import_Data(path)
	carts, grid = Find_Carts(inputs)

	print(carts)
	

if __name__ == '__main__':
	main()
	exit(0)