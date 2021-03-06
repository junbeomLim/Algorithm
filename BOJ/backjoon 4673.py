def d(n):
    count = 0
    N = n
    while n >= 1:
        count = count + n%10
        n = n//10
    return count + N
num = []
for i in range(1,10000):
    if num.count(d(i)) < 1:
        num.append(d(i))
for i in range(1,10000):
    if num.count(i) < 1:
        print(i)