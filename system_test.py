import numpy
import random
import csv
import re
from random import randint



my_data = []
with open("restaurantDatabase.txt", "r") as restaurants:
	lines = restaurants.readlines()

for line in lines:
	restaurant = line.split('\t')
	restaurant[4] = restaurant[4].replace("\n","")
	my_data.append(restaurant)
#print(my_data)

my_data = my_data[1:]

state_best_action_map = {}

#System Actions
action_value_map = {}

action_value_map["REQUEST_FOOD_TYPE"] = 0
action_value_map["REQUEST_PRICE"] = 1
action_value_map["REQUEST_LOCATION"] = 2
action_value_map["EXPLICIT_CONFIRM_FOOD"]  = 3
action_value_map["EXPLICIT_CONFIRM_PRICE"] = 4
action_value_map["EXPLICIT_CONFIRM_LOCATION"] = 5


food_type =["any","Italian","Japanese","Chinese","Mexican","Greek"]
price = ["any" , "cheap" , "medium priced" , "expensive"]
location = ["any", "Marina Del Rey", "Venice", "Santa Monica", "Korea Town","Playa Vista","Hollywood"]
confirmation = ["yes" , "no"]

slots = [" ", " ", " "]


with open('policy-submitted.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		else:			
			state = str(row[0]) + str(row[1]) +str(row[2]) +str(row[3]) +str(row[4]) +str(row[5])
			state_best_action_map[state] = str(row[6])		
			line_count += 1


def Natural_Language_Generation(action):

	if action == "REQUEST_FOOD_TYPE":
		generated_request_message = "What type of food do you want?"

	elif action == "REQUEST_PRICE":
		generated_request_message = "How expensive a restaurant do you want?"

	elif action == "REQUEST_LOCATION" :
		generated_request_message = "Where would you like the restaurant to be located?"

	elif action == "EXPLICIT_CONFIRM_FOOD":
		generated_request_message = "Did you choose %s type of food restaurant? Please confirm food type?" % slots[0]

	elif action == "EXPLICIT_CONFIRM_PRICE":
		generated_request_message = "Did you choose %s restaurant? Please confirm price." % slots[1]

	elif action =="EXPLICIT_CONFIRM_LOCATION":
		generated_request_message = "Did you choose %s location? Please confirm location"% slots[2]	

	print(generated_request_message)



def Natural_Language_Understanding(currstate,action,response):
	
	response= re.sub('[^A-Za-z0-9]+', " ", response) 
	next_state = currstate	

	if action == "REQUEST_FOOD_TYPE": 
		for food in food_type:	
			if len(re.findall('\\b'+food+'\\b', response, flags=re.IGNORECASE)) > 0:
				slots[0] = food		
				next_state = "1" + currstate[1:]

	elif action == "REQUEST_PRICE":    	
		for p in price:	
			if len(re.findall('\\b'+p+'\\b', response, flags=re.IGNORECASE)) > 0:
				slots[1] = p		
				next_state = currstate[0:1] + "1" + currstate[2:]

	elif action == "REQUEST_LOCATION":    	
		for loc in location:	
			if len(re.findall('\\b'+loc+'\\b', response, flags=re.IGNORECASE)) > 0:
				slots[2] = loc		
				next_state = currstate[0:2] + "1" + currstate[3:]

	elif action == "EXPLICIT_CONFIRM_FOOD":    	
		for msg in confirmation:	
			if len(re.findall('\\b'+msg+'\\b', response, flags=re.IGNORECASE)) > 0:				
				if msg.lower() == "no":
					slots[0] = " "
					next_state = "0" + currstate[1:3] + "0" + currstate[4:]

				else:
					next_state = currstate[0:3] + "1" + currstate[4:]

	elif action == "EXPLICIT_CONFIRM_PRICE":    	
		for msg in confirmation:	
			if len(re.findall('\\b'+msg+'\\b', response, flags=re.IGNORECASE)) > 0:				
				if msg.lower() == "no":
					slots[1] = " "
					next_state =currstate[0:1] + "0" + currstate[2:4] +"0" +currstate[5:]

				else:
					next_state = currstate[0:4] + "1" + currstate[5:]

	elif action == "EXPLICIT_CONFIRM_LOCATION":    	
		for msg in confirmation:	
			if len(re.findall('\\b'+msg+'\\b', response, flags=re.IGNORECASE)) > 0:				
				if msg.lower() == "no":
					slots[2] = " "
					next_state =currstate[0:2] + "0" + currstate[3:5] +"0" 

				else:
					next_state = currstate[0:5] + "1"
	
	return next_state

	
state = "000000"
while state != "111111":
	Natural_Language_Generation(state_best_action_map[state])	
	state = Natural_Language_Understanding(state,state_best_action_map[state],input())

d1,d2,d3 = [],[],[]

if slots[0] == "any":
	d1 = my_data
else:
	for d in my_data:	 
		if d[2] == slots[0]:
			d1.append(d)

if slots[1] == "any":
	d2 = d1
else:
	for d in d1:	 
		if d[3] == slots[1]:
			d2.append(d)

if slots[2] == "any":
	d3 = d2
else:
	for d in d2:	 
		if d[4] == slots[2]:
			d3.append(d)
if len(d3) == 0:
	print("I found no restaurants that satisfy your constraints.")
else:
	print("I found %d restaurants matching your query"% len(d3))
	for d in d3:
		print("%s is an %s %s restaurant in %s. The phone number is %s."% (d[0] ,d[3],d[2] ,d[4] ,d[1]))
	