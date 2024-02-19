tel = {
    'jack': 4098, 'sape': 4139
}
tel['guido'] = 4125
del tel['jack']
print(list(tel))
print('guido' not in tel)

a = {x : x**2 for x in (2,4,6)}
print(a)

x = dict(hello=5, ride=4, uno=3)
print(x)