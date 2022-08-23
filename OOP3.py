class math:
    @staticmethod
    def add(x,y):
        return x + y

    @staticmethod
    def add5(num):
        return num + 5

    @staticmethod
    def add10(num):
        return num + 10

    @staticmethod
    def PI():
        return 3.14

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __str__(self):
        return f'Pizza ingredients are {self.ingredients}'

    def area(self):
        return Pizza.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.PI()

p = Pizza(6, ['mozzarilla', 'tomatoes'])
print(p.area())
print(Pizza.circle_area(4))