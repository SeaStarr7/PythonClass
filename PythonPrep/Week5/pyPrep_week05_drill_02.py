#
#       Write a function that asks the user for a single character and returns it, 
#       if they put in more than one character return False
# --------------------------------------------------------------------------------------




def single():
    char = input("enter a single character")
    if len(char) > 1:
        return False
    else:
        return char
    



print(single())





