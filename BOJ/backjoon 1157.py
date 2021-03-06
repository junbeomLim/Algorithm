a = list(input().upper())
max = 0
b = []
for i in a:
    if b.count(i) < 1:
        b.append(i)
for i in b:
    if max < a.count(i):
        max = a.count(i)
num = []
for i in b:
    if max == a.count(i):
        num.append(i)
if len(num) > 1:
    print('?')
else:
    print(num[0])