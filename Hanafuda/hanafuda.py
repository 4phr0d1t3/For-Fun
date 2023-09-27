# %%
import time
import random

# %%
deck = [
    ['kasu', 'kasu', 'akatan', 'shiko'], # January
    ['kasu', 'kasu', 'akatan', 'tane'], # February
    ['kasu', 'kasu', 'akatan', 'hanami'], # March
    ['kasu', 'kasu', 'tane', 'tanzaku'], # April
    ['kasu', 'kasu', 'tanzaku', 'tane'], # May
    ['kasu', 'kasu', 'aotan', 'inoshikacho'], # June
    ['kasu', 'kasu', 'tanzaku', 'inoshikacho'], # July
    ['kasu', 'kasu', 'tane', 'tsukimi'], # August
    ['kasu', 'kasu', 'aotan', 'sake'], # September
    ['kasu', 'kasu', 'aotan', 'inoshikacho'], # October
    ['kasu', 'tanzaku', 'tane', 'ameshiko'], # November
    ['kasu', 'kasu', 'kasu', 'shiko'], # Dicember
]

months = ['January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December']

# %%
def shuffleDeck():
	coordsOfDeck = []
	for i in range(12):
		for j in range(4):
			coordsOfDeck.append([i, j])

	random.shuffle(coordsOfDeck)

	return coordsOfDeck

# %%
def startGame():
	shuffledDeck = shuffleDeck()
	
	table = []
	handP1 = []
	handP2 = []

	for i in range(8):
		table.append(shuffledDeck.pop(0))
		handP1.append(shuffledDeck.pop(0))
		handP2.append(shuffledDeck.pop(0))
	
	return shuffledDeck, table, handP1, handP2

# %%
def yaku(captured, justObtained):
	if justObtained != 0:
		for i in justObtained:
			if(
				(i == 0 and captured[0] >= 10) or
				((i == 1 or i == 9 or i == 10) and captured[i] == 4) or
				((i == 2 or i == 6 or i == 11) and captured[i] >= 5) or
				((i == 3 or i == 4 or i == 7 or i == 8) and captured[i] >= 3) or
				(i == 5 and captured[5] == 6)
				):
				return 1
	return 0

# %%
def showState(table, hand):
	print("\nTable:")
	for i in range(len(table)):
		print('\t', months[table[i][0]], '|', deck[table[i][0]][table[i][1]])

	print("\nHand:")
	for i in range(len(hand)):
		print('\t', i+1, '.', months[hand[i][0]], '|', deck[hand[i][0]][hand[i][1]])

# %%
def isPlayable(table, month):
	index = []
	for i in range(len(table)):
		if table[i][0] == month:
			index.append(i)
	if len(index) > 0:
		return index
	return 0

# %%
def updateTable(tableOrHand, capture, card, month):
	justAdded = []
	typeOfCard = deck[tableOrHand[card][0]][tableOrHand[card][1]]
	match typeOfCard:
		case 'kasu':
			capture[0] += 1
			justAdded.append(0)
		case 'akatan':
			capture[2] += 1
			capture[3] += 1
			capture[5] += 1
			justAdded.append(2)
			justAdded.append(3)
			justAdded.append(5)
		case 'shiko':
			capture[8] += 1
			capture[9] += 1
			capture[10] += 1
			capture[11] += 1
			justAdded.append(8)
			justAdded.append(9)
			justAdded.append(10)
			justAdded.append(11)
		case 'tane':
			capture[6] += 1
			justAdded.append(6)
		case 'hanami':
			capture[8] += 1
			capture[9] += 1
			capture[10] += 1
			capture[11] += 1
			capture[13] += 1
			justAdded.append(8)
			justAdded.append(9)
			justAdded.append(10)
			justAdded.append(11)
			justAdded.append(13)
		case 'tanzaku':
			capture[2] += 1
			justAdded.append(2)
		case 'aotan':
			capture[2] += 1
			capture[4] += 1
			capture[5] += 1
			justAdded.append(2)
			justAdded.append(4)
			justAdded.append(5)
		case 'inoshikacho':
			capture[6] += 1
			capture[7] += 1
			justAdded.append(6)
			justAdded.append(7)
		case 'tsukimi':
			capture[8] += 1
			capture[9] += 1
			capture[10] += 1
			capture[11] += 1
			capture[12] += 1
			justAdded.append(8)
			justAdded.append(9)
			justAdded.append(10)
			justAdded.append(11)
			justAdded.append(12)
		case 'sake':
			capture[6] += 1
			capture[12] += 1
			capture[13] += 1
			justAdded.append(6)
			justAdded.append(12)
			justAdded.append(13)
		case 'ameshiko':
			capture[10] += 1
			capture[11] += 1
			justAdded.append(10)
			justAdded.append(11)
		case _:
			print('Unknown')

	if tableOrHand[card][0] == month:
		capture[1] += 1
		justAdded.append(1)
	
	return justAdded

# %%
def playCard(hand, capture, table, month, fromHand):
	if fromHand == 'yes':
		time.sleep(1)
		card = int(input("\nEnter the card to play: "))
		card -= 1
		print("\nFrom Hand: [", months[hand[card][0]], '|', deck[hand[card][0]][hand[card][1]], ']')
	else:
		card = fromHand - 1
		print("\nFrom Deck: [", months[hand[card][0]], '|', deck[hand[card][0]][hand[card][1]], ']')

	index = isPlayable(table, hand[card][0])
	if(index == 0):
		table.append(hand.pop(card))

	elif(len(index) < 3):
		for i in index:
			print(i, '.', deck[table[i][0]][table[i][1]])
		justAdded = []
		time.sleep(1)
		cardOnTheTable = int(input("\nWhich card to capture: "))
		
		justAdded.extend(updateTable(table, capture, cardOnTheTable, month))
		table.pop(cardOnTheTable)
		
		justAdded.extend(updateTable(hand, capture, card, month))
		hand.pop(card)

		return justAdded
	elif(len(index) == 3):
		justAdded = []
		for i in index:
			print(i, '.', deck[table[i][0]][table[i][1]])
			justAdded.extend(updateTable(table, capture, i, month))

		table.pop(index[0])
		table.pop(index[1]-1)
		table.pop(index[2]-2)

		justAdded.extend(updateTable(hand, capture, card, month))
		hand.pop(card)

		return justAdded
	return 0

# %%
def play(table, hand, captured, month):
	showState(table, hand)

	index1 = playCard(hand, captured, table, month, 'yes')
	hand.append(shuffledDeck.pop(0))
	index2 = playCard(hand, captured, table, month, len(hand))

	if yaku(captured, index1) == 1 or yaku(captured, index2) == 1:
		return 1
	return 0

# %%
def getPoints(table, captured, points):
	if(captured[0] > 9):
		points += captured[0] - 9
		print('Plants')
	if(captured[1] > 3):
		points += 4
		print('Monthly card')
	if(captured[2] > 4):
		points += captured[2] - 4
		print('Ribbons')
	if(captured[3] > 2):
		points += 6 + captured[2] - 3
		print('Poetry Ribbons')
	if(captured[4] > 2):
		points += 6 + captured[2] - 3
		print('Blue Ribbons')
	if(captured[5] > 5):
		points -= captured[2]
	if(captured[6] > 4):
		points += captured[6] - 4
		print('Animals')
	if(captured[7] > 2):
		points += 5 + captured[6] - 3
		print('Boar, Deer and Butterflies')
	if(captured[8] == 3):
		points += 6
		print('3 Brights')
	if(captured[9] == 4):
		points += 10
		print('4 Brights')
	if(captured[10] == 4):
		points += 8
		print('Rainy 4 Brights')
	if(captured[11] == 5):
		points += 15
		print('5 Brights')

	rain = 0
	fog = 0

	for card in table:
		if(card[0] == 10):
			rain = 1
		if(card[0] == 11):
			fog = 1

	if(captured[12] == 2 and fog == 0):
		points += 5
		print('Moonviewing with sake')
	if(captured[13] == 2 and rain == 0):
		points += 5
		print('Flowerviewing with sake')

	return points

# %%
import os

pointsP1 = 0
pointsP2 = 0

for month in range(12):
	shuffledDeck, table, handP1, handP2 = startGame()

	capturedP1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	capturedP2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	index = []
	roundOver = 0
	print('\n[ Month |', months[month], ']')

	while(len(handP2) > 0):
		if(roundOver == 0):
			os.system('cls')
			print("\n[ Turn Player 1 ]")
			roundOver = play(table, handP1, capturedP1, month)
		else:
			print("\n[ Player 2 yaku! ]")
			koiKoi = int(input("[ Koi-Koi? | 0:No/1:Yes ] "))
			if(koiKoi == 0):
				print("\n[ Player 2 won! ]")
				pointsP2 = getPoints(table, capturedP2, pointsP2)
				print('[ Player 2 points :', pointsP2, ']')
				break
			roundOver = 0

		if(roundOver == 0):
			os.system('cls')
			print("\n[ Turn Player 2 ]")
			roundOver = play(table, handP2, capturedP2, month)
		else:
			print("\n[ Player 1 yaku! ]")
			koiKoi = int(input("[ Koi-Koi? | 0:No/1:Yes ] "))
			if(koiKoi == 0):
				print("\n[ Player 1 won! ]")
				pointsP1 = getPoints(table, capturedP1, pointsP1)
				print('[ Player 1 points :', pointsP1, ']')
				break
			roundOver = 0

	roundOver = 0
	print("\n[ Round Over ]")
print("\n[ Game Over ]\n")
print("Player 1 points :", pointsP1)
print("Player 2 points :", pointsP2, '\n')


