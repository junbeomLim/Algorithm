N = int(input())
Flower = []
for i in range(N):
    a,b,c,d = map(int, input().split())
    start = 100*a+b
    finish = 100*c+d
    Flower.append([start,finish])
Flower.sort(key=lambda x : (x[0],x[1]))
sim = 301
maximum = 301
count = 0
j = 0
while j < N:
    if sim < Flower[j][0] and maximum < Flower[j][0]:
        count = 0
        break
    if Flower[j][0] <= sim and Flower[j][1] > sim:
        if maximum < Flower[j][1]:
            maximum = Flower[j][1]
        if Flower[j][1] > 1130:
            break 
    elif Flower[j][0] > sim:
        sim = maximum
        count += 1
        j -= 1
    j += 1
    
if maximum > 1130:
    count += 1
if maximum <= 1130:
    count = 0
print(count)