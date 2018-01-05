# K Nearest Neighbors (only 23 lines of code!!!)

from operator import itemgetter

class Elem:
    def __init__ (self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

def pdist (p1, p2):
    return ((p2.y-p1.y)**2+(p2.x-p1.x)**2)**(1/2.0)

def getNeighbors (points, newpoint, k):
    distances = []
    for p in points:
        distances.append((p, pdist(newpoint, p)))
    distances.sort(key=itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0].label)
    return neighbors

def getMajority (neighbors):
    return max(set(neighbors), key=neighbors.count)

# Executable Code

points = [Elem(0.05, 0.1, 'Non-Cancerous'), Elem(0.3, 0.4, 'Non-Cancerous'), Elem(0.4, 0.3, 'Non-Cancerous'), Elem(0.5, 0.5, 'Cancerous'), Elem(0.6, 0.8, 'Cancerous')]
newpoint = Elem(0.5, 0.4, 'no label')
k = 1

print('k = {}'.format(k))
print('The new point should be labeled: {}'.format(getMajority(getNeighbors(points, newpoint, k))))
