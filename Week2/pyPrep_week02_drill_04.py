#
#       Ask the user for a string at least 10 characters long, then, print every other character.
#       If the string isn't at least 10 characters print "You are a dissapointment"
#-----------------------------------------------------------------------------------------------------



a_string = input("gimme ya string ")
if len(a_string) >= 10:
    print(a_string[::2])
else:
    print("You are a dissapointment")





