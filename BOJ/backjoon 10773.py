stack = []
K = int(input())
for i in range(0,K):
    money = int(input())
    if money != 0:
        stack.append(money)
    else:
        stack.pop()
print(sum(stack))