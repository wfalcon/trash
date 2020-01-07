import vsearch

result = vsearch.search4letters('test','iye')
if result:
	print(result)
else:
	print('Совпадений не найдено')

print(help(vsearch))