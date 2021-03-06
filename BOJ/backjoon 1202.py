import heapq
heap = []
N, K = map(int,input().split())
jewelry = []
for _ in range(N):
    M, V = map(int,input().split())
    jewelry.append((M,V))
C = []
for _ in range(K):
    C.append(int(input()))
jewelry.sort(key=lambda x: -x[0])
C.sort()
value = 0
for i in C:
    while jewelry and i >= jewelry[-1][0]:
        heapq.heappush(heap,(-jewelry[-1][1],jewelry[-1][1]))
        jewelry.pop()
    if heap:
        value += heapq.heappop(heap)[1]
    elif not jewelry:
      break
print(value)
#가방 작은 순으로 정렬
#가방 무게보다 작으면 우선순위 큐에 넣기(가격 순) 그리고 pop