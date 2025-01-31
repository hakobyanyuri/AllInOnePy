import random

class Point3D:
    """
    A class representing a 3D point with x, y, and z coordinates.
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def set_coords(self, x, y, z):
        """Sets new coordinates for the 3D point."""
        self.x = x
        self.y = y
        self.z = z
    
    def get_coords(self):
        """Returns the current coordinates as a tuple."""
        return (self.x, self.y, self.z)

class Point:
    """
    A class representing a 2D point with x and y coordinates.
    Can be initialized with another Point instance.
    """
    def __init__(self, x=0, y=0, other=None):
        if other is not None:
            self.x = other.x
            self.y = other.y
        else:
            self.x = x
            self.y = y

# List to store Point3D objects
rows = []
n = int(input("Please write the quantity of cycles"))  # Number of iterations

# Loop to create and modify Point3D objects
for _ in range(n):
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    
    # Create a new Point3D object
    point3d = Point3D(x, y, z)
    rows.append(point3d)
    print(f"Initial (x={x}, y={y}, z={z})")
    
    # Modify the coordinates attribute dynamically
    setattr(point3d, 'coords', [random.randint(1000, 5000), y, z])
    print(f"Updated (x={point3d.coords[0]}, y={y}, z={z})")

# Attempt to delete the z-coordinate from dynamically added 'coords' attribute
for point3d in rows:
    try:
        del point3d.coords[2]  # Attempt to remove the third element (z-coordinate)
    except Exception as error:
        print(f"Error: {error}")
    
    # Check if 'coords' attribute still exists
    print(hasattr(point3d, 'coords'))

# Print the original coordinates of all stored points
for p in rows:
    print("Coordinates:", p.get_coords())
