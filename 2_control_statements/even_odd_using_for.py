import time
startTime = time.time()
num = int(input("Enter the number you want to find : "))
for i in range(1, num+1):
    if i % 2 == 0:
        print("The number ", i, "is even")
    else:
        print("The number", i, "is odd")
endTime = time.time()
totalTime = endTime - startTime

print("Total time required to execute code is= ", totalTime)

