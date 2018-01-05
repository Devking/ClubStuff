# https://www.jdoodle.com/python3-programming-online

# Part 3
# KNN w/ k = 1

## Provided Code
## Don't worry about what this does!

class Elem:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def __repr__(self):
        return '({}, {}): {}'.format(self.x, self.y, self.label)

    def __str__(self):
        return '({}, {}): {}'.format(self.x, self.y, self.label)

def pdist (p1, p2):
    return distance(p1.x, p1.y, p2.x, p2.y)

def distance (x1, y1, x2, y2):
    return ((y2-y1)**2+(x2-x1)**2)**(1/2.0)

## Code to Modify
## Psst, look back to Part 2!

def closest (points, newpoint):
    closestpoint = points[0]
    closestdist = pdist(points[0], newpoint)

    for p in points:
        cdist = pdist(p, newpoint)
        # What should the if statement below use?
        if cdist < closestdist:
            closestpoint = p
            closestdist = cdist

    return closestpoint

## Executable Code
## Notice these points are the same as the ones we saw in the slides!

points = [Elem(0.05, 0.1, 'Non-Cancerous'), Elem(0.3, 0.4, 'Non-Cancerous'), Elem(0.4, 0.3, 'Non-Cancerous'), Elem(0.5, 0.5, 'Cancerous'), Elem(0.6, 0.8, 'Cancerous')]
newpoint = Elem(0.5, 0.4, 'no label')

closestpoint = closest(points, newpoint)
print('The new point should be labeled: {}'.format(closestpoint.label))

# Is this what you expected the closest point to be?
# Try it out for different new points!
