def d(n):
    count = 0
    N = n
    while n >= 1:
        count = count + n%10
        n = n//10
    return count + N
N = int(input())
a = False
for i in range(1,1000001):
    if d(i) == N:
        a = True
        break
if a == False:
    print('0')
else:
    print(i)