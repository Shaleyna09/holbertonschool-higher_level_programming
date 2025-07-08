#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
            result1 += c
    print('{}'.format(result1))
