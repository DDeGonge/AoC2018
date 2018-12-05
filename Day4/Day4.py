import sys
from collections import defaultdict

def Import_Data(path):
	f = open(path, 'r')
	return f.read().split('\n')

def Sort(data):
	data = [x.strip() for x in data]
	data = sorted(data)
	return data

def Get_sleepy(data):
	guards = [0]*5000
	guardlist = set()
	gid = 0
	lasttime = 0
	for line in data:
		if 'Guard' in line:
			gid = int(line.split('#')[1].split(' ')[0])
			guardlist.add(gid)
		elif 'falls asleep' in line:
			lasttime = int(line[15:17])
		elif 'wakes up' in line:
			nowtime = int(line[15:17])
			guards[gid] += nowtime - lasttime

	most = max(guards)
	return guards.index(most), guardlist

def Get_Best_Time(data, gid):
	sleepyhours = [0] * 60
	collect = 0
	lasttime = 0
	for line in data:
		if 'Guard' in line:
			thisID = int(line.split('#')[1].split(' ')[0])
			if gid == thisID:
				collect = 1
			else:
				collect = 0
		elif (collect == 1) and ('falls asleep' in line):
			lasttime = int(line[15:17])
		elif (collect == 1) and ('wakes up' in line):
			nowtime = int(line[15:17])
			for i in range(lasttime, nowtime):
				sleepyhours[i] += 1
	return sleepyhours.index(max(sleepyhours)), max(sleepyhours)


def main():
	path = sys.argv[1]
	data = Import_Data(path)
	sortedData = Sort(data)
	sleepy, guardlist = Get_sleepy(sortedData)
	print(sleepy)

	mosttimes = 0
	savehim = 0
	striketime = 0
	print(guardlist)
	for guard in guardlist:
		stime, strike = Get_Best_Time(sortedData, guard)
		print(guard, stime, strike)
		if stime > mosttimes:
			mosttimes = stime
			striketime = strike
			savehim = guard

	print(guard, striketime, mosttimes)
	

if __name__ == '__main__':
	main()
	exit(0)