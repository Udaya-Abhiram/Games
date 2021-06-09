money = 15

def balance():
	global user_input
	print(f"you have {money}")
	print("it's $5 to play")
	user_input = input("pick rock,paper,scissor: ")

def player_move():
	if user_input in ("ROCK","rock","r","R"):
		return "rock"
	elif user_input in ("PAPER",'P','paper','p'):
		return "paper"
	elif user_input in ("SCISSOR",'S','scissor','s'):
		return "scissor"
	else :
		return False

def computer_move():
	import random
	rps = ("rock","paper","scissor")
	comp = random.choice(rps)
	return comp

def check_winner():
	global money
	player = player_move()
	computer = computer_move()

	if player == False:
		print("please pick rock ,paper,scissor")
		thth
	elif player == "rock" and computer == "rock":
		print('\n you:' ,player)
		print('\n computer: ', computer, '\n its a draw.\n')
	elif player == "scissor" and computer == "rock":
		print("\n you: " ,player)
		print("\n computer:", computer,"\n computer wins.\n")
		money -= 5
	elif player =="paper" and computer == "rock":
		print("\n you:", player)
		print('\n computer:',computer,"\n player wins.\n")
		money += 5

	elif player == "paper" and computer == "paper":
		print('\n you:' ,player)
		print('\n computer: ', computer, '\n its a draw.\n')
	elif player == "rock" and computer == "paper":
		print("\n you: " ,player)
		print("\n computer:", computer,"\n computer wins.\n")
		money -= 5
	elif player =="scissor" and computer == "paper":
		print("\n you:", player)
		print('\n computer:',computer,"\n player wins.\n")
		money += 5

	elif player == "scissor" and computer == "scissor":
		print('\n you:' ,player)
		print('\n computer: ', computer, '\n its a draw.\n')
	elif player == "paper" and computer == "scissor":
		print("\n you: " ,player)
		print("\n computer:", computer,"\n computer wins.\n")
		money -= 5
	elif player =="rock" and computer == "scissor":
		print("\n you:", player)
		print('\n computer:',computer,"\n player wins.\n")
		money += 5
	


	
title = " *** Rock-Paper-Scissors ***"
print("-"*len(title))
print(title)		
print("-"*len(title))

while money > 0:
	balance()
	player_move()
	computer_move()
	check_winner()


print("you don't have any money left")
