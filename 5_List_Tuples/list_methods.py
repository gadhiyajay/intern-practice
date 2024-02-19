fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
vegetables = ['lemon', 'tomato', 'potato']
fruits.append('dragonfruit')
print("Appending dragon fruit in list", fruits)
fruits.extend(vegetables)
print("Extending the list", fruits)
fruits.remove("apple")  #removed the first occurence of the apple.
print("After removing", fruits)
fruits.pop(2)
print("After Pop", fruits)
apples = fruits.count('apple')
print("counting apples", apples)    # here apple is 1 because we poped one apple!
fruits.sort()
print("After Sorting", fruits)
fruits.reverse()
print("After reversing", fruits)
#print(fruits.clear())
new = fruits.copy()
print("New", new)