#!/usr/bin/env python3

import sys

#Stephen Robinson
#CSCI 373 - Cybersecurity
#February 24, 2020
#Task 2

#import task1_lib as t1
from task2_lib import *


def main():
    en_or_de = input("Encrypt (1) or Decrypt (2)") 
    # print("got : '{0}'".format(end_or_de) ) #{0} works with .format

    multiplier = int(input("Enter multiplier"))
    offset = int(input("Enter offset"))

    if en_or_de == '1':
        print("Encrypting")
        key = create_enc_key(multiplier, offset)

        if len(sys.argv) < 2:
            raise Exception("Need a plaintext file as first argument")
        plaintext_file = sys.argv[1]
        with open(plaintext_file, 'r') as fd:
            plaintext = fd.read()
            cyphertext = encrypt(plaintext, key)
            print(cyphertext)

    else:
        print("Decrypting")
        key = create_dec_key(multiplier, offset)

        if len(sys.argv) < 2:
            raise Exception("Need a plaintext file as first argument")
        plaintext_file = sys.argv[1]
        with open(plaintext_file, 'r') as fd:
            plaintext = fd.read()
            cyphertext = encrypt(plaintext, key)
            #Create file, store message
            with open("task3_decrypted_message.txt", "a") as fd:
                fd.write(cyphertext)
            print(cyphertext)

if __name__=="__main__":
    main()
