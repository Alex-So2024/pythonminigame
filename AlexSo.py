import random
#print("Hi")

#firstNumber = int(input("what is first number? "))
#secondNumber = int(input("What is second number? "))

#length = int(input("what is the length: "))
#width = int(input("what is width: "))
#calculateArea = length * width
#print("the area of your rectangle is: " + str(calculateArea))

#def calculateArea(length, width):
	#return length * width
#print(calculateArea(2,3))



humanNumber = int(input("what is your # guess?: "))
computerNumber = random.randrange(1,10)
print(str(computerNumber))

while humanNumber != computerNumber:
	if humanNumber > computerNumber:
		print("you guessed too high, try going lower")
		humanNumber = int(input("try again: "))
	if humanNumber < computerNumber:
		print("you guessed too low, try guessing higher")
		humanNumber = int(input("try again: "))

print("good job you guessed the number!")







