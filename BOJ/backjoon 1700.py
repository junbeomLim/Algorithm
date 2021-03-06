N, K = map(int, input().split())
name = [0 for _ in range(K)]
name = list(map(int, input().split()))
concent = [0 for i in range(N)]

i,j = 0,0
count = 0
for j in range(K):
    if concent.count(name[j]) > 0:
        continue
    elif concent[-1] == 0:
        concent[i] = name[j]
        i += 1
    else:
        count += 1
        order = 0
        A = True
        for k in concent:
            if name[j+1:].count(k) == 0:
                concent.remove(k)
                A = False
                break
            elif order < name.index(k,j+1):
                order = name.index(k,j+1)
        if A:
            concent.remove(name[order])
        concent.append(name[j])
print(count)
# 2 3 2 3 1 2 7 1 3 3 3 3 3
# name 뒤에 남아있는 아이 중, 먼저 오는 애를 유지. 