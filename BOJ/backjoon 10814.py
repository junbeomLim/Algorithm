N = int(input())
a = []
for i in range(N):
    age, name = input().split(' ')
    a.append((int(age),i,name))
a.sort(key=lambda x : (x[0],x[1]))
for j in a:
    print(j[0],j[2])