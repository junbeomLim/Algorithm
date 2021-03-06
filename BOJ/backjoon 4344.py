C = int(input())
for j in range(C):
    case = [0 for i in range(1000)]
    case = list(map(int,input().split(' ')))
    N = case[0]
    score = []
    score = [0 for i in range(N)]
    score = case[1:N+1]
    average = sum(score)/N
    count = 0
    for i in score:
        if i > average:
            count = count + 1
    print('%.3f' %round(count/N*100, 3)+'%')