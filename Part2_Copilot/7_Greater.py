# Please write a program which asks for two integer numbers. 
# The program should then print out whichever is greater.
# If the numbers are equal, the program should print a different message.

# Some examples of expected behaviour:

# Sample output
# Please type in the first number: 5
# Please type in another number: 3
# The greater number was: 5

# Sample output
# Please type in the first number: 5
# Please type in another number: 8
# The greater number was: 8

# Sample output
# Please type in the first number: 5
# Please type in another number: 5
# The numbers are equal!

# Write your code here:

first_number = int(input("Please type in the first number: "))
second_number = int(input("Please type in another number: "))
if first_number > second_number:
    print("The greater number was:", first_number)
elif second_number > first_number:
    print("The greater number was:", second_number)
else:
    print("The numbers are equal!")
    