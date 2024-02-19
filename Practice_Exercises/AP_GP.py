# Arithmetic Progression
# a => starting point, d => difference
# Geometric Progression
# r => common ratio
a = int(input("Enter the starting point of AP :"))
d = int(input("Enter the difference between each points in AP :"))
r = int(input("Enter the common ratio for GP :"))
temp = a
ap = [a]
gp = [a]
for i in range(a, a+10):
    a = a + d
    ap.append(a)
print("AP :", ap)

for i in range(temp, temp+10):
    temp = temp * r
    gp.append(temp)
print("GP :", gp)
