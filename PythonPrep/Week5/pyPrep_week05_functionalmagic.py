
# main: This is the most important function because it is responsible for calling your other functions in the right order. 
# There are two strategies for writing it: A) build it up incrementally as you write the other functions, or B) write this 
# function only after you have implemented all the other functions. Most students follow approach B, but if it helps you to 
# understand where each function fits into the program as you go, you might try approach A.

# print_introduction: This prints a brief message that greets the user. It consumes nothing and returns nothing.

# input_name: This prompts the user to type in their name and prints some messages (including the user's name). It consumes 
# nothing but returns the user's name as a string.

# calculate_rating: This is Grindlehook's function. Do not worry about how this function works, simply know that when its called, 
# you pass it a name as a string and it returns the customer's rating as an integer. You will only be able to call it once per 
# program's execution (afterward it stops returning the right value). You cannot simply hardcode its value into your system, 
# because it is different for each user. And, of course, you can't fix it because Grindlehook will get angry at you. On the plus 
# side, you don't have to do anything with this function besides call it in the proper place.

# print_rating: This prints the user's calculated rating (the result of calling calculate_rating). It consumes an integer 
# (representing the rating) and returns nothing.

# input_loan_amount: This prompts the user to type in their desired loan amount and prints some messages. It consumes nothing but 
# returns the loan amount as an integer. Remember, the input function returns a string, so you will need to convert the result 
# using the built-in int function. For now, you need not worry if the user types an invalid number.

# print_loan_availability: This function consumes a rating and a loan amount, and prints whether or not a loan is available to 
# the user by calling the test_loan function. It does not return anything.

# test_loan: This function consumes a rating and a loan amount, and returns whether or not a loan is available to the user by using 
# the following formula: rating2 * 100 >= loan amount. Note that this function returns a boolean, and does not print anything. 
# Don't just copy and paste in the formula. Think about what it means and write the necessary Python expression(s) to properly 
# implement it in your function.

# print_conclusion: This prints a brief message that thanks the user. It consumes nothing and returns nothing.



## 1) Define main function

## 2) Define print_introduction function

## 3) Define input_name function

## 5) Define print_rating function

## 6) Define input_loan_amount function

## 8) Define test_loan function

## 7) Define print_loan_availability function

## 9) Define print_conclusion function

## 4) Calculating Rating (already complete!)
# The following is Grindlehook's function. Do not modify it.
# You should not worry about HOW it works, but instead think of its
# arguments and return value. Remember you can only call it once!
# Do not worry that it is below the rest of your code (why does it work?).
# Do NOT change the following function definition
def calculate_rating(name):
    '''
    Returns the customer's credit rating, according to the bank's current
    status, the customer, and the alignment of the stars. This function
    is delicate, and will break after being called once.

    Notes:
        (ghook@1/15/2018): DO NOT TOUCH THIS, I FINALLY GOT IT WORKING.

    Args:
        name (str): A string representing the user's full name.
    Returns:
        int: An integer (0-9) representing the customer's credit rating.
    '''
    c=calculate_rating;setattr(c,'r',lambda:setattr(c,'o',True))
    j={};y=j['CELESTIAL_NAVIGATION_CONSTANT']=10
    j[True]='CELESTIAL_NAVIGATION_CONSTANT'
    x=str(''[:].swapcase);y=y+11,y+9,y+-2,y+-2,y+4,y+-5,y+-1,y+11,y+9,\
    y+-6,y+-6,y+-1,y+-5,y+3,y+-7,y+7,y+-1,y+-5,y+8,y+-7,y+11,y+1
    z=lambda x,t,o=0:''.join(map(lambda j:x.__getitem__(j+o), t))
    if hasattr(c,'o')and not getattr(c, 'o'): return z(x,y)
    c.o=False;j['CELESTIAL_NAVIGATION_CONSTANT'].bit_length
    d=(lambda:(lambda:None))()();g=globals()
    while d:g['X567S-lumos-17-KLAUS']=((d)if(lambda:None)else(j))
    p=lambda p:sum(map(int, list(str(p))))
    MGC=p(sum(map(lambda v: v[0]*8+ord(v[1]), enumerate(name))))
    while MGC>10:MGC=p(MGC)
    if c:return MGC
# Do NOT change the preceding function definition

# The following lines of code are used to call the main function.
# Professional Python programmers always guard their main function call with
#   this IF statement, to make it easier for other users to call their code.
# For now, just leave this code alone, but recognize that it is how you are
#   calling your main function.