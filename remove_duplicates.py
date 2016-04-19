A = [1, 2, 1, 2, 3, 4, 5]
B = []

for i in A:
    if i not in B:
        B.append(i)
print(B)
