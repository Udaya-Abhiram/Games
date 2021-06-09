score = 1

def u_input():
		global user_input
		print(f"Initial score of player  is {score}")
		user_input = input("player scored : ")

def player_move():
		if user_input in ('1','one'):
			return '1'
		elif user_input in ('2','two'):
			return '2'
		elif user_input in ('3','three'):
			return '3'
		elif user_input in ('4','four'):
			return '4'
		elif user_input in ('5','five'):
			return '5'
		elif user_input in ('6','six'):
			return '6'
		else :
			return False

def computer_move():
		import random
		number = ('1','2','3','4','5','6')
		comp = random.choice(number)
		return comp

def check_winner():
		global score
		player = player_move()
		computer = computer_move()

		if player == False:
			print("enter the numbers")
		elif player == '1' and computer == '1' :
			print("you: " ,player)
			print("computer:", computer)
			print('player is out')
			score = 0
		elif player == '2' and computer == '1':
			score +=1
			print("you: " ,player)
			print("computer:", computer)
			print("play the game")
		elif player == '3' and computer == '1':
			score +=1
			print("you: " ,player)
			print("computer:", computer)
			print("play the game")
		elif player == '4' and computer == '1':
			score +=1
			print("you: " ,player)
			print("computer:", computer)
			print("play the game")
		elif player == '5' and computer == '1':
			score +=1
			print("you: " ,player)
			print("computer:", computer)
			print("play the game")
		elif player == '6' and computer == '1':
			score +=1
			print("you: " ,player)
			print("computer:", computer)
			print("play the game")

		elif player == '1' and computer == '2' :
			print("you: " ,player)
			print("computer:", computer)
			print('play the game')
			score +=1
		elif player == '2' and computer == '2':
			print("you: " ,player)
			print("computer:", computer)
			score = 0
			print("player is out")
		elif player == '3' and computer == '2':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '4' and computer == '2':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '5' and computer == '2':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '6' and computer == '2':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")

		elif player == '1' and computer == '3' :
			print("you: " ,player)
			print("computer:", computer)
			print('play the game')
			score +=1
		elif player == '2' and computer == '3':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '3' and computer == '3':
			print("you: " ,player)
			print("computer:", computer)
			score = 0
			print("player is out")
		elif player == '4' and computer == '3':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '5' and computer == '3':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '6' and computer == '3':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")

		elif player == '1' and computer == '4' :
			print("you: " ,player)
			print("computer:", computer)
			print('play the game')
			score += 1
		elif player == '2' and computer == '4':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '3' and computer == '4':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '4' and computer == '4':
			print("you: " ,player)
			print("computer:", computer)
			score = 0
			print("player is out")
		elif player == '5' and computer == '4':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '6' and computer == '4':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")

		elif player == '1' and computer == '5' :
			print("you: " ,player)
			print("computer:", computer)
			print('play the game')
			score += 1
		elif player == '2' and computer == '5':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '3' and computer == '5':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '4' and computer == '5':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '5' and computer == '5':
			print("you: " ,player)
			print("computer:", computer)
			score = 0
			print("player is out")
		elif player == '6' and computer == '5':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")

		elif player == '1' and computer == '6' :
			print("you: " ,player)
			print("computer:", computer)
			print('play the game')
			score += 1
		elif player == '2' and computer == '6':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '3' and computer == '6':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '4' and computer == '6':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '5' and computer == '6':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '6' and computer == '6':
			print("you: " ,player)
			print("computer:", computer)
			score = 0
			print("player is out")
		else :
			print(end)


title = """ *** Cricket *** """
print('*'*len(title))
print(title)
print('*'*len(title))

while score >0 :
	u_input()
	player_move()
	computer_move()
	check_winner()
