N = int(input())
def is_group(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[j] == s[i] and j == i+1:
                break
            elif s[j] == s[i]:
                return False
    return True
count = 0
for i in range(N):
    s = list(input())
    if is_group(s) == True:
        count = count + 1
print(count)