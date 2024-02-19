#compare both list and append if the x has square in y!
res = []
for x in [1, 2, 5, 6, 3, 4]:
    for y in [8, 1, 25, 64, 3, 4]:
        if y == x**2:
            res.append((x, y))

print(res)

#using list comprehension
final = [(x, y) for x in [1, 2, 5, 6, 3, 4] for y in [8, 1, 25, 64, 3, 4] if y == x**2]
print("Using List comprehension", final)