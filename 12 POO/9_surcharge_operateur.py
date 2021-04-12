# On veut parfois définir un comportement pout les opérateurs au sein d'une classe, pour des questions de lisibilité et de compréhension.
# On peut alors "surcharger" les opérateurs correspondant.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point: [x={self.x}, y={self.y}]"

    def __add__(self, b):
        v = Vector(self.x + b.x, self.y + b.y)
        return v


a = Vector(2, 3)
b = Vector(4, -2)

c = a + b

print(c)
