import sys
S = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline())
cursor = []
for _ in range(M):
    cursor.append(sys.stdin.readline().rstrip())
K = []

for i in range(M):
    if cursor[i] == 'L':
        if len(S) != 0:
            K.append(S[-1])
            S.pop(-1)

    elif cursor[i] == 'D':
        if len(K) != 0:
            S.append(K[-1])
            K.pop(-1)

    elif cursor[i] == 'B':
        if len(S) != 0: 
            S.pop(-1)
    else:
        X = cursor[i].split()
        S.append(X[1])
K.reverse()
print(''.join(S+K))