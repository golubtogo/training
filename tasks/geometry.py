__author__ = "Nataliya"

from geom2d.point import *

a = Point(0, 0)
b = Point(6, 7)

print(a.distance(b))

l1 = [Point(3, 1), Point(0, 0), Point(1, 2)]


l2 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))
print(l1)
print(l2)

# l = [Point(i, i*i) for i in range(-5, 6)]
l = list(map(lambda i: Point(i, i*i), range(-5, 6)))


# for el in l:
#     l2.append(Point(el.x, -el.y))

# l2 = list(map(lambda p: Point(p.x, -p.y), l))
l2 = list(filter(lambda p: p.x % 2 == 0, l))

print(l)
print(l2)

l1 = [Point(0, 0), Point(1, 2), Point(2, 1)]
l2 = sorted(l1)
print("ok")
