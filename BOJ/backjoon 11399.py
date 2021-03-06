N = int(input())
time = [0 for i in range(0,N)]
time = list(map(int, input().split(' ')))
time.sort()
sum = 0
for i in range(0,len(time)):
    sum = sum + time[i]*(len(time)-i)
print(sum)