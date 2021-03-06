namerge = []
for i in range(10):
    N = int(input())
    if namerge.count(N%42) < 1:
        namerge.append(N%42)
print(len(namerge))