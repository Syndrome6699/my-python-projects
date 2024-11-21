def jumble_solver():

	dict = {}
	file = open('words.txt', 'r')

	for word in file:
		word = word.strip().lower()
		sorted_word = ''.join(sorted(word))
		if sorted_word in dict:
			if word not in dict[sorted_word]:
				dict[sorted_word].append(word)
		else:
			dict[sorted_word] = [word]

	while (True):
		jumble = input("Enter a jumbled word to decode or 'quit': ")
		jumble = jumble.lower()
		if jumble == 'quit':
			break
		jumble = ''.join(sorted(jumble))
		if jumble in dict:
			results = dict[jumble]
			for result in results:
				print(result)
			print('')
		else:
			print('results for jumble not found')


jumble_solver()