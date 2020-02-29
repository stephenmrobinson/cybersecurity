#!/usr/bin/env python3

import sys

#Stephen Robinson
#CSCI 373 - Cybersecurity
#February 24, 2020
#Task 3


#import task3_lib
from task3_lib import *


def main():
    menu_option = input("Addition (1) or Double (2) or Scalar Muliplication(3)") 

    if menu_option == '1':
        x1 = int(input("Input x1: "))
        y1 = int(input("Input y1: "))

        x2 = int(input("Input x2: "))
        y2 = int(input("Input y2: "))

        added_points = addition(x1, y1, x2, y2)
        print(added_points)

    elif menu_option == '2':
        x1 = int(input("Input x: "))
        y1 = int(input("Input y: "))

        doubled_point = double_point(x1, y1)
        print(doubled_point)

    else:
        x1 = int(input("Input x: "))
        y1 = int(input("Input y: "))
        k = int(input("Input scalar (k): "))

        multiplied_point = scalar_multiply(x1, y1, k)
        print(multiplied_point)

if __name__=="__main__":
    main()
