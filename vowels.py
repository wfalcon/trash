# vowels = ['a','e','i','o','u']
# word ="Milliwayoso"
# found=[]
# for letter in word:
# 	if letter in vowels and letter not in found:
# 		found.append(letter)
# for i in found: 
# 	print(i)
vowels = ('a','e','i','o','u')
word = "Milliwayosoee"
i = set(vowels).intersection(set(word))
for i in i:
	print(i)
print(type(vowels))