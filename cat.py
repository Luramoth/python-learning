try:
	file = open(input("give me a filename: "))

	for line in file:
		line = line.rstrip()

		print(line)
except:
	print("error: file not found")