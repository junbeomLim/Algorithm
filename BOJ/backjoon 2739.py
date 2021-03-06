#f(a, b) a * 1 부터 a * b를 출력하는 함수
def f(N,M):
    if M == 1:
        print(N,'*',1,'=',N)
    else:
        f(N, M-1)
        print(N,'*',M,'=',N*M)
f(int(input()),9)