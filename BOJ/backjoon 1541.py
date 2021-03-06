K = input().split('-')
num = []
for i in range(len(K)):
    if K[i] == '':
        num.append(0)
    else:
        K[i] = list(map(int,K[i].split('+')))
        num.append(sum(K[i]))
sum = num[0]
for i in range(1,len(num)):
    sum = sum - num[i]
print(sum)