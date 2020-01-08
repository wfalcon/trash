data = [1, 2, 3, 4, 5, 6, 7, 8]
evens = []
for num in data:
	if not num % 2:
		evens.append(num)

print(evens)

evens_gen = [num for num in data if not num %2]

print(evens_gen)

print('*'*31)

data = [ 1, 'one', 2, 'two', 3, 'three', 4, 'four' ]
words =[]
for num in data:
	if isinstance(num, str):
		words.append(num)
print(words)

word_gen = [num for num in data if isinstance(num, str)]
print(word_gen)

print('*'*60)

data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
	title.append(word.title())
print(title)

title_gen = [word.title() for word in data]
print(title_gen)

print('*'*60)

vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Don't forget to pack your towel."
found = set()
for v in vowels:
	if v in message:
		found.add(v)
print(found)

found2 = { v for v in vowels if v in message }
print(found2)

print('*'*20)