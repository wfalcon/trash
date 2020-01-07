from datetime import datetime
import time
import random

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
 		21, 23, 25, 27, 31, 35, 37, 39, 41,
 		43, 46, 47, 49, 51 ,53, 55, 57, 59]

for num in range(5):
	right_this_minune = datetime.today().minute
	
	if right_this_minune in odds:
		print("This minute seems a litele odd.")
	else:
		print("Not an odd minute.")
	if num != 4:
		time.sleep(random.randint(1,60))
