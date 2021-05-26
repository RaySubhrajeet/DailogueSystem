import numpy
import random
from random import randint




#States Map. Maps each State to a index
state_map = {}
state_map["000000"] = 0
state_map["000001"] = 1
state_map["000010"] = 2
state_map["000011"] = 3
state_map["000100"] = 4
state_map["000101"] = 5
state_map["000110"] = 6
state_map["000111"] = 7
state_map["001000"] = 8
state_map["001001"] = 9
state_map["001010"] = 10
state_map["001011"] = 11
state_map["001100"] = 12
state_map["001101"] = 13
state_map["001110"] = 14
state_map["001111"] = 15

state_map["010000"] = 16
state_map["010001"] = 17
state_map["010010"] = 18
state_map["010011"] = 19
state_map["010100"] = 20
state_map["010101"] = 21
state_map["010110"] = 22
state_map["010111"] = 23
state_map["011000"] = 24
state_map["011001"] = 25
state_map["011010"] = 26
state_map["011011"] = 27
state_map["011100"] = 28
state_map["011101"] = 29
state_map["011110"] = 30
state_map["011111"] = 31

state_map["100000"] = 32
state_map["100001"] = 33
state_map["100010"] = 34
state_map["100011"] = 35
state_map["100100"] = 36
state_map["100101"] = 37
state_map["100110"] = 38
state_map["100111"] = 39
state_map["101000"] = 40
state_map["101001"] = 41
state_map["101010"] = 42
state_map["101011"] = 43
state_map["101100"] = 44
state_map["101101"] = 45
state_map["101110"] = 46
state_map["101111"] = 47

state_map["110000"] = 48
state_map["110001"] = 49
state_map["110010"] = 50
state_map["110011"] = 51
state_map["110100"] = 52
state_map["110101"] = 53
state_map["110110"] = 54
state_map["110111"] = 55
state_map["111000"] = 56
state_map["111001"] = 57
state_map["111010"] = 58
state_map["111011"] = 59
state_map["111100"] = 60
state_map["111101"] = 61
state_map["111110"] = 62
state_map["111111"] = 63


#Rverse state map. Maps each index to state. Used for displaying/writing text.
# state = "000000" represents 
#food not filled, price not filled, location not filled
#food not confirmed, price not confirmed and location not confirmed respectively
#
state_reverse_map = {}
state_reverse_map[0] = "0,0,0,0,0,0"
state_reverse_map[1] = "0,0,0,0,0,1"
state_reverse_map[2] = "0,0,0,0,1,0"
state_reverse_map[3] = "0,0,0,0,1,1"
state_reverse_map[4] = "0,0,0,1,0,0"
state_reverse_map[5] = "0,0,0,1,0,1"
state_reverse_map[6] = "0,0,0,1,1,0"
state_reverse_map[7] = "0,0,0,1,1,1"

state_reverse_map[8]  = "0,0,1,0,0,0"
state_reverse_map[9]  = "0,0,1,0,0,1"
state_reverse_map[10] = "0,0,1,0,1,0"
state_reverse_map[11] = "0,0,1,0,1,1"
state_reverse_map[12] = "0,0,1,1,0,0"
state_reverse_map[13] = "0,0,1,1,0,1"
state_reverse_map[14] = "0,0,1,1,1,0"
state_reverse_map[15] = "0,0,1,1,1,1"

state_reverse_map[16] = "0,1,0,0,0,0"
state_reverse_map[17] = "0,1,0,0,0,1"
state_reverse_map[18] = "0,1,0,0,1,0"
state_reverse_map[19] = "0,1,0,0,1,1"
state_reverse_map[20] = "0,1,0,1,0,0"
state_reverse_map[21] = "0,1,0,1,0,1"
state_reverse_map[22] = "0,1,0,1,1,0"
state_reverse_map[23] = "0,1,0,1,1,1"

state_reverse_map[24] = "0,1,1,0,0,0"
state_reverse_map[25] = "0,1,1,0,0,1"
state_reverse_map[26] = "0,1,1,0,1,0"
state_reverse_map[27] = "0,1,1,0,1,1"
state_reverse_map[28] = "0,1,1,1,0,0"
state_reverse_map[29] = "0,1,1,1,0,1"
state_reverse_map[30] = "0,1,1,1,1,0"
state_reverse_map[31] = "0,1,1,1,1,1"

state_reverse_map[32] = "1,0,0,0,0,0"
state_reverse_map[33] = "1,0,0,0,0,1"
state_reverse_map[34] = "1,0,0,0,1,0"
state_reverse_map[35] = "1,0,0,0,1,1"
state_reverse_map[36] = "1,0,0,1,0,0"
state_reverse_map[37] = "1,0,0,1,0,1"
state_reverse_map[38] = "1,0,0,1,1,0"
state_reverse_map[39] = "1,0,0,1,1,1"

state_reverse_map[40] = "1,0,1,0,0,0"
state_reverse_map[41] = "1,0,1,0,0,1"
state_reverse_map[42] = "1,0,1,0,1,0"
state_reverse_map[43] = "1,0,1,0,1,1"
state_reverse_map[44] = "1,0,1,1,0,0"
state_reverse_map[45] = "1,0,1,1,0,1"
state_reverse_map[46] = "1,0,1,1,1,0"
state_reverse_map[47] = "1,0,1,1,1,1"

state_reverse_map[48] = "1,1,0,0,0,0"
state_reverse_map[49] = "1,1,0,0,0,1"
state_reverse_map[50] = "1,1,0,0,1,0"
state_reverse_map[51] = "1,1,0,0,1,1"
state_reverse_map[52] = "1,1,0,1,0,0"
state_reverse_map[53] = "1,1,0,1,0,1"
state_reverse_map[54] = "1,1,0,1,1,0"
state_reverse_map[55] = "1,1,0,1,1,1"

state_reverse_map[56] = "1,1,1,0,0,0"
state_reverse_map[57] = "1,1,1,0,0,1"
state_reverse_map[58] = "1,1,1,0,1,0"
state_reverse_map[59] = "1,1,1,0,1,1"
state_reverse_map[60] = "1,1,1,1,0,0"
state_reverse_map[61] = "1,1,1,1,0,1"
state_reverse_map[62] = "1,1,1,1,1,0"
state_reverse_map[63] = "1,1,1,1,1,1"


#Parameters
NUMBER_OF_EPISODES = 6000
gamma = 0.99
TIME_OUT_STEPS = 28
ACTION_REWARD = -5
COMPLETION_REWARD = 500
NUMBER_OF_STATES = 64
NUMBER_OF_ACTION = 6

#Simulated User Actions
PROVIDE_FOOD_TYPE = 0
PROVIDE_PRICE = 1
PROVIDE_LOCATION = 2
CONFIRM_POS_FOOD = 3
CONFIRM_NEG_FOOD = 4
CONFIRM_POS_PRICE =5
CONFIRM_NEG_PRICE = 6
CONFIRM_POS_LOC = 7
CONFIRM_NEG_LOC  = 8
IRRELEVENT = 9


#System Actions
REQUEST_FOOD_TYPE = 0
REQUEST_PRICE = 1
REQUEST_LOCATION = 2
EXPLICIT_CONFIRM_FOOD  = 3
EXPLICIT_CONFIRM_PRICE = 4
EXPLICIT_CONFIRM_LOCATION = 5

#Action Map
Action_Reverse_Map = {}
Action_Reverse_Map[0] = "REQUEST_FOOD_TYPE"
Action_Reverse_Map[1] = "REQUEST_PRICE"
Action_Reverse_Map[2] = "REQUEST_LOCATION"
Action_Reverse_Map[3] = "EXPLICIT_CONFIRM_FOOD"
Action_Reverse_Map[4] = "EXPLICIT_CONFIRM_PRICE"
Action_Reverse_Map[5] = "EXPLICIT_CONFIRM_LOCATION"


Q_Values = numpy.zeros(shape=(NUMBER_OF_STATES,NUMBER_OF_ACTION))


def Simulated_User_Response(systemAction,currState):

	if systemAction == REQUEST_FOOD_TYPE:
		sampleList = [PROVIDE_FOOD_TYPE, IRRELEVENT]
		choice = random.choices(sampleList, weights=(0.8,0.2), k=1) 

	elif systemAction == REQUEST_PRICE:
		sampleList = [PROVIDE_PRICE, IRRELEVENT]
		choice = random.choices(sampleList, weights=(0.8,0.2), k=1) 

	elif systemAction == REQUEST_LOCATION:
		sampleList = [PROVIDE_LOCATION, IRRELEVENT]
		choice = random.choices(sampleList, weights=(0.8,0.2), k=1) 
	

	elif systemAction == EXPLICIT_CONFIRM_FOOD and currState[0] =="1" and currState[3]== "1" :
		sampleList = [CONFIRM_POS_FOOD, CONFIRM_NEG_FOOD, IRRELEVENT]
		choice = random.choices(sampleList, weights=(0.0,0.0,1), k=1) 

	elif systemAction == EXPLICIT_CONFIRM_FOOD and currState[0] == "0":
		sampleList = [CONFIRM_POS_FOOD,CONFIRM_NEG_FOOD, IRRELEVENT]
		choice = random.choices(sampleList, weights=(0.0,0.0,1), k=1) 

	elif systemAction == EXPLICIT_CONFIRM_FOOD :
		sampleList = [CONFIRM_POS_FOOD, CONFIRM_NEG_FOOD, IRRELEVENT]
		choice = random.choices(sampleList, weights=(0.4,0.4,0.2), k=1) 

	elif systemAction == EXPLICIT_CONFIRM_PRICE and currState[1]== "1" and currState[4] == "1":
		sampleList = [CONFIRM_POS_PRICE, CONFIRM_NEG_PRICE, IRRELEVENT]
		choice = random.choices(sampleList, weights=(0.0,0.0,1), k=1) 

	elif systemAction == EXPLICIT_CONFIRM_PRICE and currState[1] == "0":
		sampleList = [CONFIRM_POS_PRICE,CONFIRM_NEG_PRICE, IRRELEVENT]
		choice = random.choices(sampleList, weights=(0.0,0.0,1), k=1) 

	elif systemAction == EXPLICIT_CONFIRM_PRICE:
		sampleList = [CONFIRM_POS_PRICE, CONFIRM_NEG_PRICE, IRRELEVENT]
		choice = random.choices(sampleList, weights=(0.4,0.4,0.2), k=1) 

	elif systemAction == EXPLICIT_CONFIRM_LOCATION and currState[2] == "1" and currState[5] == "1":
		sampleList = [CONFIRM_POS_LOC, CONFIRM_NEG_LOC, IRRELEVENT]
		choice = random.choices(sampleList, weights=(0.0,0.0,1), k=1) 

	elif systemAction == EXPLICIT_CONFIRM_LOCATION and currState[2] == "0":
		sampleList = [CONFIRM_POS_LOC, CONFIRM_NEG_LOC, IRRELEVENT]
		choice = random.choices(sampleList, weights=(0.0,0.0,1), k=1) 

	elif systemAction == EXPLICIT_CONFIRM_LOCATION:
		sampleList = [CONFIRM_POS_LOC, CONFIRM_NEG_LOC, IRRELEVENT]
		choice = random.choices(sampleList, weights=(0.4,0.4,0.2), k=1) 
	
	return choice[0]



def getNextState(simulatedUSerResponse, currState):	 

	if simulatedUSerResponse == IRRELEVENT:
		resultantState = currState 

	elif simulatedUSerResponse == PROVIDE_FOOD_TYPE:
		resultantState = "1" + currState[1:]

	elif simulatedUSerResponse == PROVIDE_PRICE:
		resultantState = currState[:1] + "1" + currState[2:]

	elif simulatedUSerResponse == PROVIDE_LOCATION:
		resultantState = currState[:2] + "1" + currState[3:]

	elif simulatedUSerResponse == CONFIRM_POS_FOOD:
		resultantState = currState[:3] + "1" + currState[4:]

	elif simulatedUSerResponse == CONFIRM_POS_PRICE:
		resultantState = currState[:4] + "1" + currState[5:]

	elif simulatedUSerResponse == CONFIRM_POS_LOC:
		resultantState = currState[:5] + "1" 

	elif simulatedUSerResponse == CONFIRM_NEG_FOOD:
		resultantState = "0" + currState[1:3] + "0" + currState[4:]

	elif simulatedUSerResponse == CONFIRM_NEG_PRICE:
		resultantState = currState[:1] + "0" + currState[2:4] + "0" + currState[5:]

	elif simulatedUSerResponse == CONFIRM_NEG_LOC:
		resultantState = currState[:2] + "0" + currState[3:5] + "0" 
	
	return resultantState


def Q_Learning_Policy_Training():
	explore_options = ["Exploitation" , "Exploration"]
	explore_weight =  [0.75,0.25]
	f1 = open("reward-submitted.csv","w")
	f1.write("CURRENT_EPISODE_NUMBER, TOTAL_REWARD_AT_END_OF_THIS_EPISODE")
	for i in range (0,NUMBER_OF_EPISODES):
		# print(i)
		alpha = 1/( 1+ i)
		#print(alpha)
		currState = "000000"
		count = 0
		total_reward = 0

		while True:			
			count += 1
			if currState == "111111" or count >= TIME_OUT_STEPS:
				break

			choice = random.choices(explore_options, weights=explore_weight, k=1)[0]			
			state_index = state_map[currState]

			if choice == "Exploitation":				
				action = numpy.argmax(Q_Values, axis=1)[state_index]				

			else:
				action_option = [REQUEST_FOOD_TYPE, REQUEST_PRICE, REQUEST_LOCATION, EXPLICIT_CONFIRM_FOOD, EXPLICIT_CONFIRM_PRICE, EXPLICIT_CONFIRM_LOCATION]
				action = random.choice(action_option)

			nextState = getNextState(Simulated_User_Response(action,currState), currState)
			next_state_index = state_map[nextState]
			reward = ACTION_REWARD

			if nextState == "111111":
				reward += COMPLETION_REWARD
			
			max_next_state_action = numpy.argmax(Q_Values, axis=1)[next_state_index]
			Q_Values[state_index][action] = Q_Values[state_index][action] + ( alpha * (reward +  gamma * Q_Values[next_state_index][max_next_state_action] - Q_Values[state_index][action]))
			currState = nextState
			total_reward += reward

		f1.write("%d ,%d\n"%(i,total_reward))
		
	f1.close()
		

Q_Learning_Policy_Training()


f = open("policy-submitted.csv", "w")
f.write("FOOD_TYPE_FILLED, PRICE_FILLED, LOCATION_FILLED, FOOD_TYPE_CONF, PRICE_CONF, LOCATION_CONF, BEST_ACTION\n")
for i in range(Q_Values.shape[0]):
	action = numpy.argmax(Q_Values, axis=1)[i]
	if Q_Values[i][action] != 0.0 or i==63:
		print(str(	state_reverse_map[i]) +" : " + str(Q_Values[i]) +" "+ str(Action_Reverse_Map[action]))
		f.write(state_reverse_map[i] + "," + Action_Reverse_Map[action]+ "\n")
	

f.close()









