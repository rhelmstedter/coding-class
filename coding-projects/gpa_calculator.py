letters_to_points = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
    "F": 0,
}


def get_grades_from_user():
    """Create a list of grade points based on user input."""
    grades = []
    while True:
        grade = input("Enter a letter grade: ").upper().strip(" -+")
        if not grade:
            break
        elif grade not in letters_to_points:
            print(f"{grade} is not a valid grade. Please try again.")
            continue
        grades.append(letters_to_points[grade])
    return grades


def calculate_gpa(grades):
    """Calculate the grade point average for a list of grades."""
    count = len(grades)
    total = sum(grades)
    gpa = total / count
    return round(gpa, 2)


def check_if_renaissance(gpa):
    """Check if someone made renaissance or honor roll."""
    if gpa >= 3.5:
        return "Congratulations, you made honor roll."
    elif gpa >= 3.0:
        return "Congratulations, you made renaissance."
    else:
        return "You did not make renaissance, try hard for next quarter."


print(
    "Welcome to the GPA Calculator.\nEnter your letter grades to calculate your GPA.\nEnter a blank line when finished."
)
grades = get_grades_from_user()
gpa = calculate_gpa(grades)
print(f"Your GPA is: {gpa}")
print(check_if_renaissance(gpa))
