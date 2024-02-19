# 2 Human years => 10 Dog years, 1 Human year => 2 Dog Year.
humanyear = int(input("Enter Human Year :"))
dogyear = 0
if humanyear <= 0:
    print("Enter valid age!!")
elif humanyear <= 2:
    dogyear = 5 * humanyear
else:
    dogyear = 10 + (humanyear - 2) * 2
print(f"For Human Year {humanyear}, Dog is {dogyear} old!")
