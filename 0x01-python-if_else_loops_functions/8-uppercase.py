#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        if ord(letters) >= 97 and ord(letters) <= 122:
            letters = chr(ord(letters) - 32)
        print("{}".format(letters), end="")
    print()
