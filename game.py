from random import randint

choices = ["feed", "play", "touch", "happy", "bit you", "ignore"]

player_lives = 3
computer_lives = 3
total_lives = 3

player_choice = False

def winorlose(status):
	print("Oh!", status, "Would you like to capture another POKEMON?")
	choice = input("Y / N ")

	if choice == "N" or choice == "n":
		print("You chose to quit! Hope you to meet other POKEMON next time!")
		exit()
	elif choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global total_lives

		player_lives = total_lives
		computer_lives = total_lives
	else:
		print("Please choose - Y or N")
		choice = input("Y / N? ")

while player_choice is False:
	print("==================*/ Capturing a POKEMON Game /*==================")
	print("Hey!! You meet a POKEMON!!")
	print("Using the POKE Ball:", computer_lives, "/", total_lives)
	print("The POKEMON favorability:", player_lives, "/", total_lives)
	print("==================================================================")

	print("Choose your action! or type quit to exit\n")
	player_choice = input("Choose feed, play, or touch with the POKEMON: \n")

	if player_choice == "quit":
		print("You chose to quit")
		exit()

	print("user chose: " + player_choice)

	computer_choice = choices[randint(3, 5)]

	print("The POKEMON responds: " + computer_choice)

	if computer_choice == "happy":
		if player_choice == "feed" or player_choice == "play" or player_choice == "touch":
			print("Yeah~The POKEMON’s favorability is UP ^V^!!!")
			computer_lives -= 1

	elif computer_choice == "ignore":
		if player_choice == "touch":
			print("Yeah~The POKEMON’s favorability is UP ^V^!!!")
			computer_lives -= 1
		else:
			print("The POKEMON seems not happy >_<!!")
			player_lives -= 1

	elif computer_choice == "bit you":
		if player_choice == "feed" or player_choice == "play" or player_choice == "touch":
			print("The POKEMON seems not happy >_<!!")
			player_lives -= 1
		
	if player_lives == 0:
		winorlose("So sad!!! The POKEMON hates you very much!!! They gone!")

	if computer_lives == 0:
		winorlose("Congratulations! Yeah~~~~You capture the POKEMON successfully!!")

	print("The POKEMON's favorability:", player_lives)
	print("Using the POKE Balls:", computer_lives)

	player_choice =False