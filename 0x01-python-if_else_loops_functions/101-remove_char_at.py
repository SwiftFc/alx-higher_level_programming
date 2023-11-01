#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    str_result = ""

    for word in range(len(str)):
        if word != n:
            str_result += str[word]

    return str_result
