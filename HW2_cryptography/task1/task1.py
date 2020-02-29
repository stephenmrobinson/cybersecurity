#!/usr/bin/env python3

import sys

#Stephen Robinson
#CSCI 373 - Cybersecurity
#February 24, 2020
#Task 1

#import task1_lib as t1
from task1_lib import *


def main():
    en_or_de = input("Encrypt (1) or Decrypt (2)") 
    # print("got : '{0}'".format(end_or_de) ) #{0} works with .format

    if en_or_de == '1':
        print("Encrypting")
        key = create_enc_key(19)

        if len(sys.argv) < 2:
            raise Exception("Need a plaintext file as first argument")
        plaintext_file = sys.argv[1]
        with open(plaintext_file, 'r') as fd:
            plaintext = fd.read()
            cyphertext = encrypt(plaintext, key)
            print(cyphertext)

    else:
        print("Decrypting")
        key = create_enc_key(-19)

        if len(sys.argv) < 2:
            raise Exception("Need a plaintext file as first argument")
        plaintext_file = sys.argv[1]
        with open(plaintext_file, 'r') as fd:
            plaintext = fd.read()
            cyphertext = encrypt(plaintext, key)
            #Create file 'task1_decrypted_message.txt', store message
            with open("task1_decrypted_message.txt", "a") as fd:
                fd.write(cyphertext)
            print(cyphertext)

if __name__=="__main__":
    main()
