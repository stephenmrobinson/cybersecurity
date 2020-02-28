#!/usr/bin/env python3

import hashlib
import sys
import getpass
import time
import math

# Stephen Robinson
# CSCI 373.001
# HW 1 - Passwords, Hash Functions, and Password Cracking
# Task 3 - Dictionary Attack with Substitutions


def main():
    #Read in "passwords.txt"
    f = open("passwords.txt", "r")
    #Read in dictionary file
    dictionary = open("/usr/share/dict/words", "r")

    #For each line in passwords.txt, crack password using dictionary attack
    for line in f:
        t0 = time.time()

        #trimmed password is extracted from the line
        trimmed_line = line.rstrip()
        x = trimmed_line.split(":")
        trimmed_pass = x[1]

        print("looking for", trimmed_pass)
        #iterate through all possible passwords in dictionary
        dictionary.seek(0)
        for line in dictionary:
            trimmed_test_pass = line.rstrip()
            if check_pass(trimmed_pass, trimmed_test_pass):
                #password found print information
                pass_found(trimmed_test_pass, t0)
                break

        #password is not a dictionary word, try with 1 substitution
        if check_pass(trimmed_pass, trimmed_test_pass) == False:

            dictionary.seek(0)
            for line in dictionary:

                trimmed_test_pass = line.rstrip()
                if 'e' in trimmed_test_pass:
                    trimmed_test_pass = trimmed_test_pass.replace('e', '3', 1)
                    if check_pass(trimmed_pass, trimmed_test_pass):
                        pass_found(trimmed_test_pass, t0)
                        break
                    #password was incorrect - change back for next substitution
                    trimmed_test_pass = trimmed_test_pass.replace('3', 'e', 1)
                if 's' in trimmed_test_pass:
                    trimmed_test_pass = trimmed_test_pass.replace('s', '$', 1)
                    if check_pass(trimmed_pass, trimmed_test_pass):
                        pass_found(trimmed_test_pass, t0)
                        break
                    trimmed_test_pass = trimmed_test_pass.replace('$', 's', 1)
                if 'a' in trimmed_test_pass:
                    trimmed_test_pass = trimmed_test_pass.replace('a', '@', 1)
                    if check_pass(trimmed_pass, trimmed_test_pass):
                        pass_found(trimmed_test_pass, t0)
                        break
                    trimmed_test_pass = trimmed_test_pass.replace('@', 'a', 1)
                if 'b' in trimmed_test_pass:
                    trimmed_test_pass = trimmed_test_pass.replace('b', '8', 1)
                    if check_pass(trimmed_pass, trimmed_test_pass):
                        pass_found(trimmed_test_pass, t0)
                        break
                    trimmed_test_pass = trimmed_test_pass.replace('8', 'b', 1)
                if 'o' in trimmed_test_pass:
                    trimmed_test_pass = trimmed_test_pass.replace('o', '0', 1)
                    if check_pass(trimmed_pass, trimmed_test_pass):
                        pass_found(trimmed_test_pass, t0)
                        break
                    trimmed_test_pass = trimmed_test_pass.replace('0', 'o', 1)

        #password is not a dictionary word with 1 sub, try two
        if check_pass(trimmed_pass, trimmed_test_pass) == False:

            dictionary.seek(0)
            for line in dictionary:

                trimmed_test_pass = line.rstrip()
                looped_pass = trimmed_test_pass
                subs = 0

                for x in range (0,2):
                    if 'e' in looped_pass:
                        looped_pass = looped_pass.replace('e', '3', 1)
                        subs += 1
                        if subs == 2:
                            if check_pass(trimmed_pass, looped_pass):
                                pass_found(looped_pass, t0)
                                break
                    if 's' in looped_pass:
                        looped_pass = looped_pass.replace('s', '$', 1)
                        subs += 1
                        if subs== 2:
                            if check_pass(trimmed_pass, looped_pass):
                                pass_found(looped_pass, t0)
                                break
                    if 'a' in looped_pass:
                        looped_pass = looped_pass.replace('a', '@', 1)
                        subs += 1
                        if subs== 2:
                            if check_pass(trimmed_pass, looped_pass):
                                pass_found(looped_pass, t0)
                                break
                    if 'b' in looped_pass:
                        looped_pass = looped_pass.replace('b', '8', 1)
                        subs += 1
                        if subs== 2:
                            if check_pass(trimmed_pass, looped_pass):
                                pass_found(looped_pass, t0)
                                break
                    if 'o' in looped_pass:
                        looped_pass = looped_pass.replace('o', '0', 1)
                        subs += 1
                        if subs == 2:
                            if check_pass(trimmed_pass, looped_pass):
                                pass_found(looped_pass, t0)
                                break



def check_pass(trimmed_pass, trimmed_test_pass):
    spassword=hashlib.scrypt( bytes(trimmed_test_pass, 'utf-8'),
                            salt = bytes('salt', 'utf-8'),
                            n=8, r=2, p=1)
    crypted_pass = spassword.hex()
    return trimmed_pass == crypted_pass


def pass_found(trimmed_test_pass, t0):
    t1 = time.time()
    total = t1-t0

    print("The password is: ", trimmed_test_pass)
    print("Bits of Entropy: ", len(trimmed_test_pass)* math.log(94, 2))
    print("The cracking process took: ", total, " seconds. \n")


if __name__=="__main__":
    main()
