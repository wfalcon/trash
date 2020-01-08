import sys

try:
	with open('file.txt') as fh:
		file_data = fh.read()
	print(file_data)
except FileNotFoundError:
	print('The data file is missing.')
except PermissionErrorError:
	print('This is not allowed.')
except:
	print('Some other error occurred.')

print('*'*25)

try:
	1/0
except:
	print('Делили на ноль?;)')
	err = sys.exc_info()
	for e in err:
		print(e)

print('*'*25)

try:
	with open('file.txt') as fh:
		file_data = fh.read()
	print(file_data)
except FileNotFoundError:
	print('The data file is missing.')
except PermissionErrorError:
	print('This is not allowed.')
except Exception as err:
	print('Some other error occurred.', str(err))