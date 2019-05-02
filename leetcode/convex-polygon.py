'''
469. Convex Polygon


Given a list of points that form a polygon when joined sequentially, find 
if this polygon is convex (Convex polygon definition).

Note:

There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon 
(Simple polygon definition). In other words, we ensure that exactly two edges 
intersect at each vertex, and that edges otherwise don't intersect each other.
'''

def orientation(x, y, z):
    val = (y[1] - x[1])*(z[0] - y[0]) - (y[0] - x[0])*(z[1] - y[1])
    return True if val > 0 False

def process(points):
    for i in range(len(points)-2):
        if not orientation(points[i], points[i+1], points[i+2]):
            return False
    return True

def main():
    points = []
    while True:
        x = input()
        if len(input()) == 0:
            break
        points.append([int(n) for n in x.split()])

    process(points)

if __name__ == "__main__":
    main()