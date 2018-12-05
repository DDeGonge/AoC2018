import sys
import time
import csv
import numpy as np

# DATA INDICES
id0 = 'ID'
id1 = 'x start'
id2 = 'y start'
id3 = 'x end'
id4 = 'y end'

def Import_Data(path):
	f = open(path, 'r')
	return f.read().split('\n')

def Format_Data(data):
	returnData = []
	for line in data:
		entry = [-1,-1,-1,-1,-1]
		vals = line.split('@')[1].strip()
		vals = vals.split(':')

		entry[0] = int(line.split('@')[0].strip('#'))
		entry[1] = int(vals[0].split(',')[0])
		entry[2] = int(vals[0].split(',')[1])
		entry[3] = entry[1] + int(vals[1].split('x')[0]) - 1
		entry[4] = entry[2] + int(vals[1].split('x')[1]) - 1
		returnData.append(entry)
	return returnData

def Sort_By_X(data):
	datalen = len(data)
	for i in range(0, datalen - 1):
		for j in range(i, datalen):
			if data[i][1] > data[j][1]:
				temp = data[j]
				data[j] = data[i]
				data[i] = temp

	return data


def lamesearch(data):
	data = np.array(data)
	xmax = max(data[:,2])
	ymax = max(data[:,4])

	crashez = 0
	for x in range(0, xmax):
		for y in range(0, ymax):
			found = 0
			for entry in data:
				if (x >= entry[1]) and (x <= entry[3]) and (y >= entry[2]) and (y <= entry[4]):
					found += 1
			if found >= 2:
				crashez += 1

	print(crashez)

def Smarter_Search(data):
	data = np.array(data)
	xmax = max(data[:,3])
	ymax = max(data[:,4])

	nogood = [1] * (len(data) + 1)
	nogood[0] = 0
	crashez = 0
	for x in range(0, xmax):
		dataset = []
		for entry in data:
			if (x >= entry[1]) and (x <= entry[3]):
				dataset.append(entry)


		for y in range(0, ymax):
			found = 0
			IDs = []
			for entry in dataset:
				if (y >= entry[2]) and (y <= entry[4]):
					found += 1
					IDs.append(entry[0])
			if found >= 2:
				crashez += 1
				for yeet in IDs:
					nogood[yeet] = 0
	#return crashez

	print(nogood)

	good_id = []
	for i in range(0, len(nogood)):
		if nogood[i] == 1:
			good_id.append(i)

	assert len(good_id) == 1
	return good_id[0]


def main():
	path = sys.argv[1]
	data = Import_Data(path)
	data = Format_Data(data)
	#sortedData = Sort_By_X(data)
	collisions = Smarter_Search(data)
	print(collisions)

if __name__ == '__main__':
	main()
	exit(0)