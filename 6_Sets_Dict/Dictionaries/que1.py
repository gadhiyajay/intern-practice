# sort with respect to key!
my_dict = {'banana': 5, 'apple': 10, 'orange': 4, 'grapes': 6}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item:  item[1], reverse=True))
print(sorted_dict)
