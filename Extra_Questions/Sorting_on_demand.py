def sortin(num_list, wtd):
    if wtd == "asc":
        num_list.sort()
        print("The Ascending Sorted List is :", num_list)

    elif wtd == "desc":
        num_list.sort(reverse=True)
        print("The Descending Sorted List is :", num_list)

    elif wtd == "none":
        print("The Unaltered List : ", num_list)

    else:
        print("Please Enter Valid Input!")


lst1 = [2, 4, 6, 7, 2, 10]
print("Here the list to be considered is :", lst1)
whattd = input('Enter What you want to do!(asc, desc, none)')
sortin(lst1, whattd)
