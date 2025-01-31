import random

class Point3D:
    def __init__(self, x, y, z):
        self.coords = [x, y, z]
    
    def set_coords(self, x, y, z):
        self.coords = [x, y, z]
    
    def get_coords(self):
        return tuple(self.coords)

class Point:
    def __init__(self, x=None, y=None, other=None):
        if other is not None:
            self.x = other.x
            self.y = other.y
        else:
            self.x = x if x is not None else 0
            self.y = y if y is not None else 0

rows = []
n = 5
for _ in range(n):
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    point3d = Point3D(x, y, z)
    rows.append(point3d)
    print(f"Initial (x={x}, y={y}, z={z})")
    setattr(point3d, 'coords', [random.randint(1000, 5000), y, z])
    print(f"Updated (x={point3d.coords[0]}, y={y}, z={z})")

for point3d in rows:
    try:
        del point3d.coords[2]
    except Exception as error:
        print(f"Error: {error}")
    print(hasattr(point3d, 'coords'))

for p in rows:
    print("Coordinates:", p.get_coords())
