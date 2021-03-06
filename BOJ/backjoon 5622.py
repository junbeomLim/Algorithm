time = 0
s = list(input())
for i in s:
    if i == 'A' or i == 'B' or i == 'C':
        time = time + 3
    elif i == 'D' or i == 'E' or i == 'F':
        time = time + 4
    elif i == 'G' or i == 'H' or i == 'I':
        time = time + 5
    elif i == 'J' or i == 'K' or i == 'L':
        time = time + 6
    elif i == 'M' or i == 'N' or i == 'O':
        time = time + 7
    elif i == 'P' or i == 'Q' or i == 'R' or i=='S':
        time = time + 8
    elif i == 'T' or i == 'U' or i == 'V':
        time = time + 9
    elif i == 'W' or i == 'X' or i =='Y' or i == 'Z':
        time = time + 10
print(time)