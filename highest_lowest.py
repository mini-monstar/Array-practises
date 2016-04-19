array = [1,3,4,2,7,8,4]
highest = 0
lowest = 1000000
for i in array:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i

print(highest,lowest)
