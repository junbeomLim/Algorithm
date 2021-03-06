N = int(input())
word = []
for i in range(N):
    w = input()
    word.append((len(w),w))
word = list(set(word))
word.sort(key=lambda x: (x[0],x[1]))
for i in word:
    print(i[1])