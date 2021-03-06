def is_hansu(N):
    a = []
    for i in range(len(N)-1):
        if a.count(int(N[i+1]) - int(N[i])) < 1:
            a.append(int(N[i+1]) - int(N[i]))
    if len(a) > 1:
        return False
    else:
        return True
N = input()
count = 0
for i in range(1,int(N)+1):
    if is_hansu(str(i)) == True:
        count = count + 1
print(count)