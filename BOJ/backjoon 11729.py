#hanoi(start,finish,N) = 시작이 start, 끝이 finish, N개사 쌓여 있을 때 과정을 출력하는 함수
#hanoi(1,3,N) =  hanoi(1,2, N-1) 후에 N번 원반 3으로 이동, hanoi(2,3,N-1)
def hanoi(start,middle,finish,N):
    if N==1:
        print(start, finish)
    else:    
        hanoi(start,finish,middle,N-1)
        print(start, finish)
        hanoi(middle,start,finish,N-1)
K = int(input())
print(2**K-1)
hanoi(1,2,3,K)