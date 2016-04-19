A = [2,2,4,2,4]
N = 5
B = []
duplicates = 0

for i in range(N):
    B.append(i)
print(B)

for i in B:
    count = 0
    for j in range(N):
        if i == A[j]:
            count += 1
        if count == 2:
            duplicates += 1
            break

print (duplicates)
