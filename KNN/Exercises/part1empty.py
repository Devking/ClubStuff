# https://www.jdoodle.com/python3-programming-online

# Part 1
# Distance Formula

## Provided Code
## Don't worry about what this does!

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

def pdist (p1, p2):
    return distance(p1.x, p1.y, p2.x, p2.y)

## Code to Modify

def distance (x1, y1, x2, y2):
    # Modify the below line to complete the distance formula!
    return ( (y2-y1)**2 )**(1/2.0)

## Executable Code
## Don't modify the below code until you've figured
## out the modifications in the section above!

a = Point(0, 0) # Create a point at (0, 0)
b = Point(3, 4) # Create a point at (3, 4)
d = pdist(a, b) # Get the distance between the two

print(d)        # Print the distance

# Is this what you expected the distance to be?
# Is this what you expected the distance to be?
# Try this out for other points by changing the coordinates for point b!
