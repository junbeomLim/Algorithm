X = int(input())
i = 1
j = 0
while X > j:
    j = j + i
    i = i + 1
if (i-1)%2 == 1:
    print(j-X+1,end='/')
    print(j-i+1+1-(j-i+1-(X-j+i-1)+1))
else:
    print(j-i+1+1-(j-i+1-(X-j+i-1)+1),end='/')
    print(j-X+1)