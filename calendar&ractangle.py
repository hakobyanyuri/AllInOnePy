class Calendar:
    __slots__ = ['day', 'month', 'year']  # Using __slots__ to save memory by restricting attribute creation

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @property
    def day(self):
        return self._day  # Use a private attribute to avoid recursion in the property

    @day.setter
    def day(self, value):
        if value < 1:
            raise ValueError('Day must be greater than 0')
        self._day = value  # Set the private attribute

    @property
    def month(self):
        return self._month  # Use a private attribute to avoid recursion in the property

    @month.setter
    def month(self, value):
        if not (1 <= value <= 12):
            raise ValueError('Month must be in the range 1-12')
        self._month = value  # Set the private attribute

    @property
    def year(self):
        return self._year  # Use a private attribute to avoid recursion in the property

    @year.setter
    def year(self, value):
        if value < 1:
            raise ValueError('Year must be greater than 0')
        self._year = value  # Set the private attribute

    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year}"  # Format the date as DD.MM.YYYY


class CoordinateDescriptor:
    def __init__(self):
        self._values = {}  # Dictionary to store values for each instance

    def __get__(self, instance, owner):
        return self._values.get(instance, None)  # Get the value for the instance

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Coordinate must be a number")
        self._values[instance] = value  # Set the value for the instance


class Rectangle:
    x1 = CoordinateDescriptor()  # Descriptor for x1 coordinate
    y1 = CoordinateDescriptor()  # Descriptor for y1 coordinate
    x2 = CoordinateDescriptor()  # Descriptor for x2 coordinate
    y2 = CoordinateDescriptor()  # Descriptor for y2 coordinate

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"Rectangle: ({self.x1}, {self.y1}) - ({self.x2}, {self.y2})"  # Format the rectangle coordinates
