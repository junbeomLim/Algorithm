N = int(input())
for j in range(N):
    ans = input()
    score = 0
    i = 0
    while i < len(ans):
        count = 0
        while i < len(ans) and ans[i] != 'X':
            count = count + 1
            score = score + count
            i = i + 1
        i = i +1
    print(score)