# https://www.jdoodle.com/python3-programming-online

# Part 4
# KNN w/ any positive number k

## Provided Code
## Don't worry about what this does!

class Elem:
    def __init__ (self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def __repr__ (self):
        return '({}, {}): {}'.format(self.x, self.y, self.label)

    def __str__ (self):
        return '({}, {}): {}'.format(self.x, self.y, self.label)

def pdist (p1, p2):
    return distance(p1.x, p1.y, p2.x, p2.y)

def distance (x1, y1, x2, y2):
    return ((y2-y1)**2+(x2-x1)**2)**(1/2.0)

def getMajority (neighbors):
    # Notice that this doesn't deal with tie-breakers the way we did in the slides
    return max(set(neighbors), key=neighbors.count)

## Code to Modify

from operator import itemgetter

def getNeighbors (points, newpoint, k):
    distances = []
    for p in points:
        distances.append((p, pdist(newpoint, p)))
    # Take a guess what the following print command will print
    # Remove the comment so you can see the printout
    # print(distances)
    distances.sort(key=itemgetter(1))
    # Take a guess what the following print command will print
    # Remove the comment so you can see the printout
    # print(distances)
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0].label)
    # Take a guess what the following print command will print
    # Remove the comment so you can see the printout
    # Try the following print command for different k values!
    print(neighbors)
    return neighbors

## Executable Code
## Don't modify the below code until you've figured out the section above!

points = [Elem(0.05, 0.1, 'Non-Cancerous'), Elem(0.3, 0.4, 'Non-Cancerous'), Elem(0.4, 0.3, 'Non-Cancerous'), Elem(0.5, 0.5, 'Cancerous'), Elem(0.6, 0.8, 'Cancerous')]
newpoint = Elem(0.5, 0.4, 'no label')
k = 3

print('k = {}'.format(k))
print('The new point should be labeled: {}'.format(getMajority(getNeighbors(points, newpoint, k))))

# Is this what you expected the closest point to be?
# Try it out for different values of k!
# And then try it out for different points!
