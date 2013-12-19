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
    fah = float(input("Enter temperature in Fahrenheit:"))
    print("The temperature in Celsius:", fahrenheit2celcius(fah))

def fahrenheit2celcius(f):
    return 5/9 * (f - 32)

if __name__ == '__main__':
    main()
