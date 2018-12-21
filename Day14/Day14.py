import sys
import string
import numpy as np
import time

np.set_printoptions(threshold=np.inf)

def Simulate(seed, e0, e1):
	seed += str(int(seed[e0]) + int(seed[e1]))
	slen = len(seed)
	e0 = (e0 + (int(seed[e0]) + 1)) %slen
	e1 = (e1 + (int(seed[e1]) + 1)) %slen
	return seed, e0, e1
	

def BetterPrint(grid):
	for line in grid:
		thisline = ''
		for char in line:
			thisline += char
		print(thisline)


def main():
	seed = '37'
	cpos = 320851
	e0 = 0
	e1 = 1

	i = 0
	clen = len(str(cpos))
	while True:
		seed, e0, e1 = Simulate(seed, e0, e1)
		if len(seed) > 7:
			#print(seed[-6:], seed[-7:-1])
			if seed[-clen:] == str(cpos):
				print('found it')
				print(len(seed) - len(str(cpos)))
				break
			elif seed[-clen - 1:-1] == str(cpos):
				print('found it at n-1')
				print(len(seed) - len(str(cpos)) - 1)
				break
		i += 1
		print(i)

if __name__ == '__main__':
	main()
	exit(0)