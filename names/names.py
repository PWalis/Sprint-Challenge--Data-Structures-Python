import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
names_1 = sorted(names_1)
names_2 = sorted(names_2)




duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# O(n Logn)
for name_1 in names_1:
    name_2 = names_2[:]
    # this does a binary search for the name
    while len(name_2):
        if len(name_2) == 1:
            if name_1 == name_2[0]:
                duplicates.append(name_1)
                break
            else:
                break
        elif name_1 < name_2[len(name_2)//2]:
            name_2 = name_2[:len(name_2)//2]
        elif name_1 > name_2[len(name_2)//2]:
            name_2 = name_2[len(name_2)//2:]
        elif name_1 == name_2[len(name_2)//2]:
            duplicates.append(name_1)
            break
        
        

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")