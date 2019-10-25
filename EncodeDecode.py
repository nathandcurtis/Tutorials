# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:55:41 2019

@author: nathan.curtis
"""

mode = raw_input("Would you like to encode or decode? ")
key = raw_input("What is your key? ")
key = int(key)
if mode == 'encode':
    message = raw_input("Enter a message to encode: ")
    message = message.upper()
    output = ""
    for letter in message:
        if letter.isupper():
            value = ord(letter) + key
            letter = chr(value)
            if not letter.isupper():
                value -= 26
                letter = chr(value)
        output += letter
    print"Output message: ", output
else:
    message = raw_input("Enter a message to decode: ")
    message = message.upper()
    output = ""
    for letter in message:
        if letter.isupper():
            value = ord(letter) + 26 - key
            letter = chr(value)
            if not letter.isupper():
                value -= 26
                letter = chr(value)
        output += letter
    print"Output message: ", output