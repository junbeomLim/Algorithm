N = int(input())
rope = []
for i in range(N):
    rope.append(int(input()))
rope.sort()
weight = []
for i in range(N):
    weight.append(rope[i]*(N-i))
weight.sort()
print(weight[-1])