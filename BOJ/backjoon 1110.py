a = int(input())

first = a

if a < 10:
        a = a*11
else:
    a = (a % 10)*10 + (a % 10 + a//10)%10
count = 1
while first != a:
    if a < 10:
        a = a*11
    else:
        a = (a % 10)*10 + (a % 10 + a//10)%10
    count = count + 1
print(count)