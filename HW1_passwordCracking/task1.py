#!/usr/bin/env python3

import hashlib
import sys
import getpass
import math

# Stephen Robinson
# CSCI 373.001
# HW 1 - Passwords, Hash Functions, and Password Cracking
# Task 1 - Storing Username / Password Pairs

def main():
    #Get username
    print("Enter your username:", end=" ")
    sys.stdout.flush()
    username = sys.stdin.readline()
    trimmed_username = username.rstrip()
    print("Username: '"+ username + "'")
    print("Trimmed Username: '" + trimmed_username + "'")

    #Get password
    password = getpass.getpass(prompt="Enter Password: ")
    print("Password: ", password)

    spassword = hashlib.scrypt( bytes(password, 'utf-8'), 
                                salt = bytes('salt', 'utf-8'), 
                                n=8, r=2, p=1)

    crypted_password = spassword.hex()
    print("Crypted Password: ", crypted_password)

    #Create file 'passwords.txt', store username/pass
    with open("passwords.txt", "a") as fd:
        fd.write(trimmed_username + ":" + crypted_password + "\n")

    #Print entropy of password
    print("Bits of Entropy: ", len(password) * math.log(94, 2))




if __name__=="__main__":
    main()
