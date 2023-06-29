# 
#        In this drill we'll use an f-string to find the modulus of two numbers. Ask the user for two numbers,
#       then use an f-string to print "[num1] mod [num2] is equal to [remainder]"
# --------------------------------------------------------------------------------------------------------------------------


num1 = input("Gimme ya numbah")

num2 = input("Gimme ya second numbah")

remainder = int(num1) % int(num2)

print(f"{num1} mod {num2} is equal to {remainder}")





