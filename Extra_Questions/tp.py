def divisible_digits(start, end):
    return [
        n for n in range(start, end + 1)
        if not any(map(lambda x : int(x) == 0 or n % int(x) != 0, str(n)))
    ]

print(divisible_digits(1, 500))