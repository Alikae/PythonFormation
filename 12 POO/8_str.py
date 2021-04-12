class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector: [x={self.x}, y={self.y}]"

a = Vector(2, 3)

print(f"{a}")
