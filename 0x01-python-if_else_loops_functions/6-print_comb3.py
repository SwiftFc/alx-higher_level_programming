#!/usr/bin/python3
for numbers in range(10):
    for num in range(numbers + 1, 10):
        if numbers == 8 and num == 9:
            print("89")
        else:
            print("{:02d}, ".format(numbers * 10 + num), end='')
