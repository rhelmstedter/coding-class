"""GPA Calculator."""

# CONSTANTS
NUMBER_OF_CLASSES = 6

# INPUT
print("Welcome to the GPA Calculator.")
print("Enter the grade points you earned in each class.")
print("A is 4, B is 3, C is 2, D is 1, F is 0.")

points_1 = input("Grade points for class 1: ")
points_2 = input("Grade points for class 2: ")
points_3 = input("Grade points for class 3: ")
points_4 = input("Grade points for class 4: ")
points_5 = input("Grade points for class 5: ")
points_6 = input("Grade points for class 6: ")

# PROCESS
# input() always hands back a string, so every answer needs converting first.
points_1 = int(points_1)
points_2 = int(points_2)
points_3 = int(points_3)
points_4 = int(points_4)
points_5 = int(points_5)
points_6 = int(points_6)

total_points = points_1 + points_2 + points_3 + points_4 + points_5 + points_6

# Dividing an int by an int gives a float, which is what a GPA needs.
gpa = total_points / NUMBER_OF_CLASSES
gpa = round(gpa, 2)

# OUTPUT
print(f"You earned {total_points} grade points in {NUMBER_OF_CLASSES} classes.")
print(f"Your GPA is {gpa}.")
