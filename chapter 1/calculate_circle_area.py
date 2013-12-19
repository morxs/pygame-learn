#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vincent
#
# Created:     19/12/2013
# Copyright:   (c) vincent 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math

def main():
    print("Print area of circle")
    radius = float(input("Enter the radius of the circle:"))
    print("Area of the circle is:", circle_area(radius))

def circle_area(r):
    return math.pi * r ** 2

def arb_triangle_area(a, b, c):
    return .5 * a * b * math.sin(c)

if __name__ == '__main__':
    main()
