import random
import math

lowerbound = int(input("Enter Lower bound:- "))

upperbound = int(input("Enter Upper bound:- "))

x = random.randint(lowerbound, upperbound)
print("\n\tYou've only ",
	round(math.log(upperbound - lowerbound + 1, 2)),
	" chances to guess the integer!\n")


count = 0

while count < math.log(upperbound - lowerbound + 1, 2):
	count += 1

	guess = int(input("Guess a number:- "))

	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

if count >= math.log(upperbound - lowerbound + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")
