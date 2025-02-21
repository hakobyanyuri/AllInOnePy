class Table:
    # Define the attributes that instances of this class can have
    __slots__ = ('length', 'width', 'height', '__table_type')
    
    def __init__(self, l=0, w=0, h=0, t="rectangle"):
        # Initialize the table with length, width, height, and type
        self.length, self.width, self.height, self.__table_type = l, w, h, t

    def square(self):
        from math import pi
        # Lambda function to calculate the area of a rectangle
        rectangle_square = lambda : self.length * self.width
        # Lambda function to calculate the area of a round table
        round_square = lambda : pi * ((self.length / 2) ** 2)
        # Determine the type of table and return the appropriate area
        if 'round' in self.__table_type:
            return round_square()
        else:
            return rectangle_square()


class RoundTtable(Table):
    # Define the attributes that instances of this class can have
    __slots__ = '__table_type',
    
    def __init__(self, l=0, w=0, h=0):
        # Initialize the round table with the type set to "round"
        Table.__init__(self, l, w, h, "round")

class RectangleTable(Table):
    # Define the attributes that instances of this class can have
    __slots__ = '__table_type',
    
    def __init__(self, l=0, w=0, h=0):
        # Initialize the rectangle table with the type set to "rectangle"
        Table.__init__(self, l, w, h, "rectangle")


print("Class RoundTtable:")
# Create an instance of RoundTtable and print its area
round_t = RoundTtable(1000, 1000, 700)
print(round_t.square())

print("\nClass RectangleTable:")
# Create an instance of RectangleTable and print its area
rect_t = RectangleTable(1000, 1000, 700)
print(rect_t.square())

print("\nClass Table:")
# Create instances of Table with different types and print their areas
t1 = Table(1000, 1000, 700, "round")
print(t1.square())
t2 = Table(1000, 1000, 700, "rectangle")
print(t2.square())