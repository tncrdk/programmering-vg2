Collection = [False, True]
print(Collection)
x = len(Collection)
sequence = 0
Summary = []
for z in range(6):
    if x == 1:
        if Collection[sequence] == False:
            print("E")
            Summary.append("E")
        elif Collection[sequence] == True:
            print("T")
            Summary.append("T")
    elif x == 2:
        if Collection[sequence] == False:
            sequence += 1
            if Collection[sequence] == False:
                print("I")
                Summary.append("I")
            elif Collection[sequence] == True:
                print("A")
                Summary.append("A")
        elif Collection[sequence] == True:
            sequence += 1
            if Collection[sequence] == False:
                print("D")
                Summary.append("D")
            elif Collection[sequence] == True:
                print("I don't know")
    elif x == 3:
        if Collection[sequence] == False:
            if Collection[sequence] == False:
                if Collection[sequence] == False:
                    print()
    sequence = 0
Collection.clear()
print(Summary)
