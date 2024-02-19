first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("Is the first set subset of second?", first_set.issubset(second_set))
print("Is the second set subset of first?", second_set.issubset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print(first_set)
print(second_set)