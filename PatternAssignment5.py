start = 1
stop = 2
lastnumber = stop
for row in range(2, 6):
    for col in range(start, stop):
        lastnumber -= 1
        print(lastnumber, end=" ")
    print("")
    start = stop
    stop += row
    lastnumber = stop
