wordsfile = open('test.txt')

words = list

for line in wordsfile:
	print(line.split())

	yeah = line.split()

	words.append(yeah)

print(words)