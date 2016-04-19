A = [1,2,3,4,5]
integer = 6
for i in A:
    found = False
    if integer == i:
        print("YES")
        found = True
        break 
if not found:
    print("no")
