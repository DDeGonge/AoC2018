import sys
import string
import numpy as np
import time

np.set_printoptions(threshold=np.inf)

def Import_Data(path):
	f = open(path, 'r')
	return f.read().strip().split('\n')

def Generate_Grid(strings):
	arr = []
	for line in strings:
		oneline = []
		for char in line:
			oneline.append(char)
		arr.append(oneline)
	print(arr)
	return np.array(arr)

def Count_Adjacent(grid, x, y, xlim, ylim):
	ymin = y - 1
	if ymin < 0:
		ymin = 0
	ymax = y + 1
	if ymax > ylim:
		ymax = ylim
	xmin = x - 1
	if xmin < 0:
		xmin = 0
	xmax = x + 1
	if xmax > xlim:
		xmax = xlim

	rangearr = grid[xmin:xmax + 1, ymin:ymax + 1]
	ntree = 0
	nlumber = 0
	for line in rangearr:
		for char in line:
			if char == '|':
				ntree += 1
			elif char == '#':
				nlumber += 1

	if grid[x,y] == '|':
		ntree -= 1
	elif grid[x,y] == '#':
		nlumber -= 1

	return ntree, nlumber

def Count_All(grid):
	ntree = 0
	nlumber = 0
	for line in grid:
		for char in line:
			if char == '|':
				ntree += 1
			elif char == '#':
				nlumber += 1

	return ntree, nlumber


def Simulate(grid):
	newgrid = []
	xlim = len(grid)
	ylim = len(grid[0])
	
	for x, line in enumerate(grid):
		newline = []
		for y, char in enumerate(line):
			ntree, nlumber = Count_Adjacent(grid, x, y, xlim, ylim)
			
			if char == '.':
				if ntree >= 3:
					newline.append('|')
				else:
					newline.append('.')
			elif char == '|':
				if nlumber >= 3:
					newline.append('#')
				else:
					newline.append('|')
			elif char == '#':
				if ntree == 0 or nlumber == 0:
					newline.append('.')
				else:
					newline.append('#')

		newgrid.append(newline)

	return np.array(newgrid)

def BetterPrint(grid):
	for line in grid:
		thisline = ''
		for char in line:
			thisline += char
		print(thisline)


def main():
	path = sys.argv[1]
	data = Import_Data(path)
	grid = Generate_Grid(data)
	for i in range(0, 1281):
		newgrid = Simulate(grid)
		print(i)
		ntree, nlumber = Count_All(grid)
		print(ntree, nlumber, ntree * nlumber)
		BetterPrint(newgrid)
		grid = newgrid

	ntree, nlumber = Count_All(grid)
	print(ntree, nlumber, ntree * nlumber)
	

if __name__ == '__main__':
	main()
	exit(0)