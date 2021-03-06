N = int(input())
able = [0,1,2]
for i in range(3,N+1):
    able.append((able[i-1]+able[i-2]) % 15746)
print(able[N])