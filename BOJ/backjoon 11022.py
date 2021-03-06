import sys
N = int(sys.stdin.readline())
for i in range(1,N+1):
    a,b = map(int, sys.stdin.readline().split(' '))
    sys.stdout.write('Case #'+str(i)+': '+str(a)