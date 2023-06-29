#
#       In the united states you must be 18 years old or older to vote in an election
#       Write a program that asks the user for their age, and then prints "You get to vote"
#       or "Too young to vote", depending on their age. If the age is greater than 120, 
#       print "How are you not dead???"
#------------------------------------------------------------------------------------------------


age = input("Wat is your age???? ")
age = int(age)


if age < 18:
    print("To young to vote")

if age >= 18 and age < 120:
    print("you get to vote")

if age > 120:
    print("How are you not dead!?!?!?!")