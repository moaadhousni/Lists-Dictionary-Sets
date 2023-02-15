#Problem 4

sentence = input("enter a sentence")
word_dict = {}

for word in sentence.split():
	if word in word_dict:
		word_dict[word] += 1
	else:
		word_dict[word] = 1
print(f'{"WORD":<12}COUNT')
for word, value in sorted(word_dict.items()):
	print(f'{word:<12}{value}')

print('\nNumber of Unique Words:',len(word_dict))

def max_count(word_dict):
	max_value = 0
	for key in word_dict:
		count = word_dict[key]
		if count >= max_value:
			max_value = count
		else:
			continue
	for key in word_dict:
		if word_dict[key] == max_value:
			print(f'{"WORD":<5}COUNT')
			print(key, ' ',max_value)

def min_count(word_dict):
	min_value = 1
	for key in word_dict:
		count = (word_dict[key])
		if count <= min_value:
			min_value = count
		else:
			continue
	for key in word_dict:
		if word_dict[key] == min_value:
			print(f'{"WORD":<5}COUNT')
			print(key, ' ',min_value)

max_count(word_dict)
min_count(word_dict)
