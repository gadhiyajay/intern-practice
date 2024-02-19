sample_dict = {'a': 100, 'b': 200, 'c': 300}
a = int(input("Enter the value you want to find :"))
if a in sample_dict.values():
    print(f"{a} found")
else:
    print(f"{a} Not found")