#Problem 3

text=input('string value')

split_text = text.split()
word =set()
for i in split_text:
	if i in word:
		continue
	else:
		word.add(i)
print(word)






