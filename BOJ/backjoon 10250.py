T = int(input())
H = []
W = []
N = []
for i in range(0,T):
    h, w,n = map(int,input().split())
    H.append(h)
    W.append(w)
    N.append(n)

for i in range(0,T):
    if N[i]%H[i] != 0:
        print((N[i]%H[i])*100+N[i]//H[i]+1)
    else:
        print(H[i]*100+N[i]//H[i])