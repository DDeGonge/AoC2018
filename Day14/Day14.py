import sys
import string
import numpy as np
import time

np.set_printoptions(threshold=np.inf)

def Simulate(seed, e0, e1):
	a, b = divmod(seed[e0] + seed[e1], 10)
	if a:
		seed.append(a)
	seed.append(b)

	slen = len(seed)
	e0 = (e0 + seed[e0] + 1) %slen
	e1 = (e1 + seed[e1] + 1) %slen
	return seed, e0, e1
	

def BetterPrint(grid):
	for line in grid:
		thisline = ''
		for char in line:
			thisline += char
		print(thisline)


def main():
	seed = [3,7]
	cpos = [3,2,0,8,5,1]
	e0 = 0
	e1 = 1

	i = 0
	clen = len(cpos)
	while True:
		seed, e0, e1 = Simulate(seed, e0, e1)
		if len(seed) > 7:
			#print(seed[-6:], seed[-7:-1])
			if seed[-clen:] == cpos:
				print('found it')
				print(len(seed) - clen)
				break
			elif seed[-clen - 1:-1] == cpos:
				print('found it at n-1')
				print(len(seed) - clen - 1)
				break
		i += 1
		print(i)

if __name__ == '__main__':
	main()
	exit(0)