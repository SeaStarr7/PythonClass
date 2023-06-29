#       Ask the user for a integer, and use a for loop to print the following sequence.
#       (in this example the number the user entered was 5)
#
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# --------------------------------------------------------------------------------------------



user_num = int(input("I need a number "))

empty_string = ""
for i in range(1, user_num + 1):
    empty_string = empty_string + str(i)
    print(empty_string)













