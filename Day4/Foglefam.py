import sys
import re
from collections import *
from math import *

def Import_Data(path):
	f = open(path, 'r')
	return f.read().split('\n')

def main():
    lines = Import_Data(sys.argv[1])
    lines = [x.strip() for x in lines]
    lines = list(filter(None, lines))
    lines = sorted(lines)

    guards = defaultdict(lambda: defaultdict(int))
    asleep = defaultdict(int)
    for line in lines:
        print(line)
        if 'begins shift' in line:
            id = re.findall(r'\#\d+', line)
            id = int(id[0][1:])
        if 'falls asleep' in line:
            h0 = int(line[12:14])
            m0 = int(line[15:17])
        if 'wakes up' in line:
            h1 = int(line[12:14])
            m1 = int(line[15:17])
            while True:
                if h0 == h1 and m0 == m1:
                    break
                if h0 == 0:
                    guards[id][m0] += 1
                    asleep[id] += 1
                m0 += 1
                if m0 >= 60:
                    m0 = 0
                    h0 += 1
    #print(guards)
    print(sorted(asleep.items(), key=lambda x: x[1]))
    print(sorted(guards[499].items(), key=lambda x: x[1]))
    for id in guards.keys():
    	hi = sorted(guards[id].items(), key=lambda x: x[1])[-1]
    	print(id, hi)

if __name__ == '__main__':
    main()