PI = 3.14159


def get_number():
    # add your exception handling code here
    number = float(input("Please enter a number: "))
    return number


def calculate_circle_area(radius: float) -> float:
    # add your exception handling code here
    return PI * radius * radius
