import random
from PIL import Image
from colorama import Fore
from colorama import Back, Style
imgAlcaraz = Image.open("Alcaraz.webp")
imgDjokovic = Image.open("Djokovic.webp")
imgMedvedev = Image.open("Medvedev.jpeg")
imgFederer = Image.open("Federer.webp")
imgNadal = Image.open("Nadal.webp")
def clueOneTwoThree(userClue):
	for x in range(userClue):
		userChoice = int(input("Enter 1 for country, 2 for current Ranking, 3 for play style, 4 for special traits, or 5 for notable achievements: "))

		if userChoice == 1:
			print(countryValue)
		elif userChoice == 2:
			print(currentRankingValue)
		elif userChoice == 3:
			print(playStyleValue)
		elif userChoice == 4:
			print(specialTraitsValue)
		elif userChoice == 5:
			print(notableAchievementsValue)
		else:
			print("invalid number")

playerList = ["Djokovic", "Federer", "Nadal", "Alcaraz", "Medvedev"]

country = {
	"Djokovic":"Serbia",
	"Federer":"Switzerland",
	"Nadal":"Spain",
	"Alcaraz":"Spain",
	"Medvedev":"Russia"
}

currentRanking = {
	"Djokovic":"2",
	"Nadal":"139",
	"Federer":"currently retired but career high #1 in 2004",
	"Alcaraz":"1",
	"Medevedev":"3"
}

playStyle = {
	"Djokovic":"He's a baseline player. Hard courts favor his playstyle",
	"Nadal":"A heavy hitter with much spin. Clay courts favor his playstyle",
	"Federer":"A swift and powerful stroke. Grass courts favor his playstyle",
	"Alcaraz":"An intense and extremely strong player. Usually hard courts favor his playstyle",
	"Medvedev":"Plays behind the baseline usually. Usually hard courts favor his playstyle as he is defensive"
}

specialTraits = {
	"Djokovic":"Known for his textbook backhand motion and power",
	"Nadal":"Known for his warrior spirit and grit (never gives up no matter what)",
	"Federer":"Known as the GOAT of Tennis and went down in history as one of the most classy and sportsmanlike players ever to exist",
	"Alcaraz":"Reached the world number one ranking just 2 years after his first appearance on tour (youngest spainiard to ever reach world no. 1.)",
	"Medvedev":"Returns so far back that the camera cant even see him in the shot"
}

notableAchievements = {
	"Djokovic":"Held the world no. 1 position for the longest time in the history of Tennis",
	"Nadal":"Won a staggering 11 French Open titles throughout his career and had a career high of no. 1",
	"Federer":"Won 5 consecutive US Open titles from 2004-2008 and had a career high of no. 1",
	"Alcaraz":"Won 2 grand slam titles (US Open and Wimbledon) and is currently 20 years old",
	"Medvedev":"Won 6 consecutive tournament titles (One of them being the US Open in 2021 where he beat djokovic in straight sets)"
}



key, value = random.choice(list(country.items()))



countryValue = country.get(key)
currentRankingValue = currentRanking.get(key)
playStyleValue = playStyle.get(key)
specialTraitsValue = specialTraits.get(key)
notableAchievementsValue = notableAchievements.get(key)


print("Hello! Welcome to the Tennis player guessing game. The goal of this game is to guess the correct player based off of the hints that I give you! Try to use as little hints as possible for the best challenge! Here is the list of the players you can choose from: Djokovic, Federer, Nadal, Alcaraz, Medvedev. Be mindful of capitalization! Enjoy! :)")
print()
userClue = int(input("How many clues do you wish to ask for?: "))
print()
clueOneTwoThree(userClue)

userPlayerGuess = str(input("What is your player guess?: "))

while key != userPlayerGuess:
	userClue = str(input(Fore.RED + Style.BRIGHT + "You guessed incorrectly. Would you like another hint? (yes or no): "))
	print(Fore.RESET)
	print(Style.RESET_ALL)
	print(Back.RESET)
	if userClue == "yes":
		print("*******")
		userNextClue = int(input("How many more clues do you want?: "))
		clueOneTwoThree(userNextClue)
		userPlayerGuess = str(input("What is your player guess?: "))
	elif userClue == "no":
		userPlayerGuess = str(input("What is your player guess?: "))
	else:
		userClue = str(input("You guessed incorrectly. Would you like another hint? (yes or no): "))


if key == userPlayerGuess:
	print(Fore.GREEN + Style.BRIGHT + "You got the player correct! Congratulations!")
	print("The player was " + key + "!")
	funFact = str(input("Would you like to learn a fun fact about this player? (type yes or no): "))
	if funFact == "yes":
		if userPlayerGuess == "Djokovic":
			print("Novak knows how to speak 11 different languges! Some include Mandarin, Portuguese, Japanese, and German!")
			imgDjokovic.show()
		if userPlayerGuess == "Federer":
			print("Federer sleeps for 12 hours everyday to allow his body to fully recover!")
			imgFederer.show()
		if userPlayerGuess == "Medvedev":
			print("He studied Math at a university in Moscow before becoming a tennis pro!")
			imgMedvedev.show()
		if userPlayerGuess == "Alcaraz":
			print("He made his professional debut in 2020 at the age of 16!")
			imgAlcaraz.show()
		if userPlayerGuess == "Nadal":
			print("Nadal's hobbies include football, video games, and fishing!")
			imgNadal.show()
			



	if funFact == "no":
		if userPlayerGuess == "Djokovic":
			imgDjokovic.show()
		if userPlayerGuess == "Federer":
			imgFederer.show()
		if userPlayerGuess == "Nadal":
			imgNadal.show()
		if userPlayerGuess == "Alcaraz":
			imgAlcaraz.show()
		if userPlayerGuess == "Medvedev":
			imgMedvedev.show()


	

print(Fore.RESET)
print(Back.RESET)
print(Style.RESET_ALL)
	























