#
#       Ask the user to input a number between 1 and 10 inclusive if the number they entered 
#       is not in the desired range then contiue prompting them. (hint: you will need a 'while' loop)
#------------------------------------------------------------------------------------------------------------



user_input = int(input("give me a number between 1 and 10"))

while user_input < 1 or user_input > 10:
    user_input = int(input("Nooooo that's not right try again"))
print("You got it right yay")












