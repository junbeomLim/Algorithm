N = int(input())
stair_num = [[0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1],
[1,1,2,2,2,2,2,2,2,1]]
for i in range(3,N+1):
    stair_num.append([stair_num[i-1][1]%1000000000,
    (stair_num[i-1][0] + stair_num[i-1][2])%1000000000,
    (stair_num[i-1][1] + stair_num[i-1][3])%1000000000,
    (stair_num[i-1][2] + stair_num[i-1][4])%1000000000,
    (stair_num[i-1][3] + stair_num[i-1][5])%1000000000,
    (stair_num[i-1][4] + stair_num[i-1][6])%1000000000,
    (stair_num[i-1][5] + stair_num[i-1][7])%1000000000,
    (stair_num[i-1][6] + stair_num[i-1][8])%1000000000,
    (stair_num[i-1][7] + stair_num[i-1][9])%1000000000,
    stair_num[i-1][8]%1000000000])
print(sum(stair_num[N])%1000000000)