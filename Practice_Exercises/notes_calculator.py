# No.of notes in amount given!
count = {}
notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
amount = int(input("Enter Your Amount :"))

for note in notes:
    if amount != 0:
        if amount >= note:
            temp = amount // note
            count[note] = temp
            amount = amount % note

print(count)
