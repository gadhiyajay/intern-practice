set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
res = set1.isdisjoint(set2)
print(res)
if res:
    print("Sets have nothing common")
else:
    print('Common element in the sets are :', set1.intersection(set2))