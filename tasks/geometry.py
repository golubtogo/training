__author__ = "Nataliya"

from geom2d.point import *

a = Point(0, 0)
b = Point(6, 7)

print(a.distance(b))

l1 = [Point(0, 0), Point(1, 2), Point(2, 1)]
l2 = sorted(l1)
print("ok")
