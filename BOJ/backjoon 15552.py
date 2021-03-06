import sys
N = int(sys.stdin.readline())
for i in range(0,N):
    a,b = map(int, sys.stdin.readline().split(' '))
    sys.stdout.write(str(a+b)+'\n')