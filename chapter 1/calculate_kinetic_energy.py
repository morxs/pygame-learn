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
    print("This program calculate kinetic energy of moving object")
    m_str = input("Enter object mass in kg:")
    m = float(m_str)
    v_str= input("Enter object velocity in mps:")
    v = float(v_str)
    e = 0.5 * m * v ** 2
    print("The object has " + str(e) + " joules of energy")

if __name__ == '__main__':
    main()
