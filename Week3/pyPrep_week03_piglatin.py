#
# Pig latin is a fun psuedo language, in which English words are altered to create 'new' words
# In this assignment you'll write a program to turn regular words into pig latin using string concatination

# Pig latin rules:

# Rule One: word begins with a consonant
# If the word your translating begins with a consonant or several consonants, take however many consonants you
# have and puth them at the end of the word. Then, add 'ay' to the end of the word. As an example, dog would
# become 'ogday' and 'brush' would become 'ushbray'

# Rule Two Word beings with a vowel
# If the word you're translating starts with a vowel then all you need to do is add 'hey' on the end of the 
# word. For example, 'elephant' would become 'elephanthey' and 'air' would become 'airhey'

# Write your code under this line.
#-------------------------------------------------------------------------------------------------------------

vowels = "aeiou"

a_word = "air"


for num in range(10):
    print(num)


if a_word[0] in vowels:
    print(a_word + "hey")
else:
    for i in range(len(a_word)):
        if a_word[i] in vowels:
            
            
            
            
            
            
            
            
            
            
            
            pig_word = a_word[i:] + a_word[0:i] + "ay"
            print(pig_word)
            break
    







    



