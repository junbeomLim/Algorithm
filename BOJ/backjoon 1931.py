num = int(input())
x_num = []
x = []

for i in range(0,num):
    x = list(map(int,input().split()))
    x.reverse()
    x_num.append(x)
x_num.sort()

count = 1
finish = x_num[0][0]
i = 1
while i < len(x_num):
    if finish <= x_num[i][1]:
        count = count + 1
        finish = x_num[i][0]
        #print(x_num[i])
    i = i +1

print(count)