from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

print(Timer('a,b = b,a', 'a=1; b=2').timeit())