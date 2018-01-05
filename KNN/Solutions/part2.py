# https://www.jdoodle.com/python3-programming-online

# Part 2
# Closest Point

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

def distance (x1, y1, x2, y2):
    return ( (y2-y1)**2 + (x2-x1)**2 )**(1/2.0)

## Code to Modify

def closest (points, newpoint):
    closestpoint = points[0]
    closestdist = pdist(points[0], newpoint)

    for p in points:
        cdist = pdist(p, newpoint)
        if cdist < closestdist:
            # Two lines should go here; can you figure them out?
            closestpoint = p
            closestdist = cdist

    return closestpoint

## Executable Code
## Don't modify the below code until you've figured
## out the modifications in the section above!

points = [Point(0,0), Point(3,4)]
newpoint = Point(3,2)

closestpoint = closest(points, newpoint)
print(closestpoint)

# Is this what you expected the closest point to be?
# Try it out for different points!
