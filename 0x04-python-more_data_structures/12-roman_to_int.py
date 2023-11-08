#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    rom_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    result = 0
    prev_val = 0

    for symbol in roman_string[::-1]:
        value = rom_dict.get(symbol, 0)
        if value < prev_val:
            result = result - value
        else:
            result = result + value
            prev_val = value
    return result
