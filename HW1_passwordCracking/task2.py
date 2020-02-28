#!/usr/bin/env python3

import hashlib
import sys
import getpass
import time
import math

# Stephen Robinson
# CSCI 373.001
# HW 1 - Passwords, Hash Functions, and Password Cracking
# Task 2 - Brute Force Attack

def main():
    #Read in "passwords.txt"
    f = open("passwords.txt", "r")

    #For each line, crack password
    for line in f:
        t0 = time.time()

        #trimmed password is extracted from the line
        trimmed_line = line.rstrip()
        x = trimmed_line.split(":")
        trimmed_pass = x[1]

        #iterate through all possible passwords starting with length 1
        test_pass = " " 
        trimmed_test_pass = test_pass.strip()
        spassword = hashlib.scrypt( bytes(trimmed_test_pass, 'utf-8'),
                                    salt = bytes('salt', 'utf-8'),
                                    n=8, r=2, p=1)
        crypted_pass = spassword.hex()
        #make test pass a string of space chars and iterate from left to right using trim to cut pass to fit
        while trimmed_pass != crypted_pass:
            #increment test_pass
            test_pass = increment_pass(test_pass)
            print("Now checking: ", test_pass)
            trimmed_test_pass = test_pass.strip()
            spassword = hashlib.scrypt( bytes(trimmed_test_pass, 'utf-8'),
                                        salt = bytes('salt', 'utf-8'),
                                        n=8, r=2, p=1)
            crypted_pass = spassword.hex()

        t1 = time.time()
        total = t1-t0
        print("The password is: ", test_pass)
        print("Bits of Entropy: ", len(trimmed_test_pass)* math.log(94, 2))
        print("The cracking process took: ", total, " seconds. \n")


def increment_pass(s):
    listed = list(s)
    for i, c in list(enumerate(listed))[::-1]:
        if listed[i] == '~':
            listed[i] = '!'
        else:
            listed[i] = chr(ord(listed[i])+1)
            #prepend a space to the list if our next call would increase the size of the password
            if all(c == '~' for c in listed):
                listed.insert(0,' ')
            new_s = ""
            return (new_s.join(listed))




if __name__=="__main__":
    main()
