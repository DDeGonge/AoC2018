import sys

def Import_Data(path):
	f = open(path, 'r')
	return f.read().split('\n')

def CountMultiples(data):
	double_count = 0
	triple_count = 0
	for line in data:
		doubles = 0
		triples = 0
		count = {}
		for s in line:
			if s in count:
				count[s] += 1
			else:
				count[s] = 1

		for key in count:
			if count[key] == 2:
				doubles = 1
			elif count[key] == 3:
				triples = 1
		double_count += doubles
		triple_count += triples

	return double_count * triple_count

def Find_Similar(data):
	numWords = len(data)
	wordLen = len(data[0])
	i = 0
	j = 0
	best = 0
	word = ''
	for i in range(0, numWords - 1):
		for j in range(i + 1, numWords):
			count = 0
			for c in range(0, wordLen):
				if data[i][c] == data[j][c]:
					count += 1
				if count > best:
					best = count
					word = [data[i], data[j]]
					print(best)

	answer = ''
	for i in range(0,wordLen):
		if word[0][i] == word[1][i]:
			answer += word[0][i]
	return answer


def main():
	path = sys.argv[1]
	data = Import_Data(path)
	checksum = CountMultiples(data)
	print(checksum)
	samesies = Find_Similar(data)
	print(samesies)

if __name__ == '__main__':
	main()
	exit(0)