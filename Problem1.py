#Problem 1

text=input('string value')
split_text = text.split()
word = []
count=0
for i in split_text:
    if i in word:
        count = count
    else:
        word.append(i)
        count += 1
print(count)
print(word)
