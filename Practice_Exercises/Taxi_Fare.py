# First 5 kms => 10rs/km, then 5 rs/km
def fair(ride):
    if ride == 0:
        print("Invalid INPUT!!")
    elif ride <= 5:
        fair = ride * 10
    else:
        fair = (ride - 5) * 5 + 50
    print(f"For {ride} km, fair is {fair}")

ride  = int(input("Enter you travel distance"))
fair(ride)


