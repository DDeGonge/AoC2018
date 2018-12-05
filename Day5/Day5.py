import sys
import string

def Import_Data(path):
	f = open(path, 'r')
	return f.read().strip()

def Trim_String(stin, tocut):
	newstring = ''
	lasti = -1
	for i in tocut:
		newstring += stin[lasti + 1:i - 1]
		lasti = i
	newstring += stin[lasti + 1:]
	return newstring

def Get_Collapsed(data):
	done = 0
	fullstring = data
	while not done:
		lastletter = ''
		done = 1
		tocut = []
		index = 0
		while index < len(fullstring):
			if (fullstring[index].lower() == lastletter.lower()) and (fullstring[index] != lastletter):
				tocut.append(index)
				index += 1 # Prevents letter triples from being removed all at once
				done = 0
			try:
				lastletter = fullstring[index]
			except:
				pass
			index += 1

		# Trim string
		if len(tocut) > 0:
			fullstring = Trim_String(fullstring, tocut)

	return fullstring

def main():
	path = sys.argv[1]
	data = Import_Data(path)

	bestresult = 9999999
	disletter = ''
	for letter in string.ascii_lowercase:
		testing = data.replace(letter.lower(), '')
		testing = testing.replace(letter.upper(), '')

		thisresult = Get_Collapsed(testing)
		if len(thisresult) < bestresult:
			bestresult = len(thisresult)
			disletter = letter

		print(letter, len(thisresult))

	print(letter)


	#data = Get_Collapsed(data)
	#print(data, len(data))
	

if __name__ == '__main__':
	main()
	exit(0)