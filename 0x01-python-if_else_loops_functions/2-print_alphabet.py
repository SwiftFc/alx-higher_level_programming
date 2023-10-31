#!/usr/bin/python3
for letter in range(ord('A'), ord('Z') + 1):
    convert_to_alpha = chr(letter)
    print(f"{convert_to_alpha.lower()}", end='')
