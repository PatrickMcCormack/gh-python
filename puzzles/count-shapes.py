#!/usr/bin/env python

"""
    count the number of shapes in an 2d array
      A distructive version.
      Limitations: designed only to count L-like shapes.
"""

import pprint

pp = pprint.PrettyPrinter(indent=4)

a = [ [0, 0, 1, 0, 0, 1, 1, 1 ],
      [1, 0, 1, 0, 0, 0, 0, 1 ],
      [1, 0, 1, 1, 1, 0, 0, 1 ],
      [1, 0, 0, 0, 0, 0, 0, 1 ],
      [1, 1, 1, 1, 1, 0, 1, 0 ],
      [0, 0, 0, 0, 0, 1, 1, 0 ] ]

def left(a,x,y):
    if x > 0:
        return a[y][x-1]

def up(a,x,y):
    if y > 0:
        return a[y-1][x]

print "-------------------------"
print "BEFORE"
pp.pprint(a)
print "------------------------------"

count=1
for y in range(len(a)):
    for x in range(len(a[0])):
        if a[y][x] == 1:
            above = up(a,x,y)
            before = left(a,x,y)
            if before > 1:
                if above > 1:
                    for repair in range(x, -1, -1):
                        if a[y][repair] != 0:
                            a[y][repair] = above
                        else:
                            break
                    else:
                        a[y][x] = before
                elif up(a, x, y, ) > 1:
                    a[y][x] = up(a, x, y)
                else:
                    count += 1
                    a[y][x] = count

print "AFTER"
pp.pprint(a)
print "------------------------------"

print "Number of shapes is ", count - 2
