import math


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p.area())
print(Pizza.area(p)) # same
print(Pizza.circle_area(8)) # static accessed independantly

# static don't access the instance
# signal to show it is independant
# don't need to worry about setting up a complete class instance before a test
# can test like a regular function
