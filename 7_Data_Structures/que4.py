# occurence of each element from the list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count_dict = dict()
for i in sample_list:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
print(count_dict)