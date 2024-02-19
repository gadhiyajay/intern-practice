import re

numbers = ["+91-4846461684", "+1-549469468", "+22-317977317973198"]


def country_code(numbers):
    pattern = r'(\+\d+)-'
    for number in numbers:
        match = re.findall(pattern, number)
        if match:
            print(f"{number} country code is {match}")

country_code(numbers)
