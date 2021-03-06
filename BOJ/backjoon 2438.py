def star(N):
    if N == 1:
        print('*')
    else:
        star(N-1)
        for i in range(N):
            print('*',end='')
        print()
N = int(input())
star(N)