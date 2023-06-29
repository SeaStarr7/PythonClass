#
#       Prompt the user to input two numbers, check if the denominator (the bottom number)
#       is 0. If it is then print "You can't divide by zero!", otherwise print the quotient.
#-----------------------------------------------------------------------------------------------------



num1 = input("Give me a number ")
num2 = input("Give me another number")

num1 = int(num1)
num2 = int(num2)

if num2 == 0:
    print("You can't divide by zero!")
else:
    print(num1 / num2)





