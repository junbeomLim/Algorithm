N = int(input())
Seq = list(map(int, input().split()))
add = [Seq[0]]
for i in range(1,N):
    add.append(max(add[i-1]+Seq[i],Seq[i]))
print(max(add))