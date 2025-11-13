# You are tasked with creating a simple grading system for a class. 
# Write a Python program that takes a student's score as input
#  and calculates and prints its corresponding letter grade based on the following grading scale:

# 90 or above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

grade = int(input("Enter the student's score: "))

if grade >=90:
    print("The grade is A")
elif grade >=80:
    print("The grade is B")
elif grade >=70:
    print("The grade is C")
elif grade >=60:
    print("The grade is D")
else:
    print("The grade is F")
