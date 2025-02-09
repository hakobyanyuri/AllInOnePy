class Person:
    """
    A class to represent a person with a name and age.
    Supports comparison based on age.
    """
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Person {self.name}, {self.age} years old'

    # Comparison methods based on age
    def __ne__(self, other) -> bool:
        return self.age != other.age

    def __lt__(self, other) -> bool:
        return self.age < other.age

    def __le__(self, other) -> bool:
        return self.age <= other.age

    def __gt__(self, other) -> bool:
        return self.age > other.age

    def __ge__(self, other) -> bool:
        return self.age >= other.age

# Creating Person instances
p1 = Person('Adam', 16)
p2 = Person('John', 14)
p5 = Person('Ann', 23)

class Vector:
    """
    A class to represent a 3D vector.
    Supports vector addition.
    """
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """Returns a new Vector as the sum of two vectors."""
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self) -> str:
        return f'Vector ({self.x}, {self.y}, {self.z})'

# Creating Vector instances
v1 = Vector(1, 2, 3)
v2 = Vector(2, 4, 7)

# Adding two vectors
res = v1 + v2
