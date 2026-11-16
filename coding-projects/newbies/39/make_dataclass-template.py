# Convert this class to a dataclass

class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __str__(self):
        return f"A rectangle with a base of {self.base} and a height of {self.height}."

    def calc_area(self):
        return self.base * self.height

    def calc_perimeter(self):
        return 2 * self.base + 2 * self.height
