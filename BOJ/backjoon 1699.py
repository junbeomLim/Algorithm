N = int(input())
som = [0 for _ in range(N+1)]
som[1] = 1 
case = []
for i in range(2,N+1):
    m = int(i**0.5)
    for j in range(m,0,-1):
        case.append(1+som[i-j**2])
    som[i] = min(case)
    case = []
print(som[N])