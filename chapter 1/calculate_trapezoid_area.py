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

def main():
    print("Area of a trapezoid")
    h = float(input("Enter the height of the trapezoid:"))
    x1 = float(input("Enter the length of the bottom base:"))
    x2 = float(input("Enter the length of the top base:"))
    print("The area is:", trapezoid_area(x1, x2, h))

def trapezoid_area(x1, x2, h):
    return 0.5 *(x1 + x2) * h

if __name__ == '__main__':
    main()
