class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calc_area(self):
        return self.base * self.height

    def calc_perimeter(self):
        return 2 * self.base + 2 * self.height

    # add the __str__ method
