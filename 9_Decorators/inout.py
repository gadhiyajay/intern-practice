# read test.txt

with open("../dhaval.txt", "r") as fp:
    # read all lines from a file

    lines = fp.readlines()


# open new file in write mode
with open("./newfile.txt", "w") as fp:
    count = 0
    # print(count)
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            #print(count)
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1
