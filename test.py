import json
import pprint
dictData = {
		   'user_1':{ "ID"       : 210450,
             "login"    : "admin",
             "name"     : "John Smith",
             "password" : "root",
             "phone"    : 5550505,
             "email"    : "smith@mail.com",
             "online"   : True },

           "user_2":{ "ID"       : 3456565,
             "login"    : "user",
             "name"     : "Bob Mitchell",
             "password" : "user",
             "phone"    : 55568798,
             "email"    : "Bob@mail.com",
             "online"   : False },
           "user_3":{ "ID"       : 6875682,
             "login"    : "falcon",
             "name"     : "Влад Сокол",
             "password" : "user",
             "phone"    : 55576453,
             "email"    : "vlad@mail.com",
             "online"   : False }
             }
jsonData = json.dumps(dictData)

with open("data.json", "w") as file:
	file.write(jsonData)

with open("data.json", "r") as file:
	jsonr=json.loads(file.read())

for key, val in jsonr.items():
		print('-'*25)
		print(key,':')
		for i in val.items():
			print('\t',i[0],'=>', i[1]) 

print('-'*25)

pprint.pprint(jsonr)
print(jsonr['user_3']['name'])