N = int(input())
A,B,C,D,E,F = map(int, input().split())
ans = 0
if N > 2:
    ans = min(A,B,C,D,E,F) * (N-2) * (5*N-6)
    ans += min(A+B,A+C,A+E,A+D,B+C,B+D,B+F,C+E,C+F,D+E,D+F,E+F) * (2*N-3) * 4
    ans += min(A+B+C,A+B+D,A+D+E,A+E+C,B+D+F,B+F+C,C+E+F,D+E+F) * 4
elif N == 2:
    ans = min(A+B,A+C,A+E,A+D,B+C,B+D,B+F,C+E,C+F,D+E,D+F,E+F) * (2*N-3) * 4
    ans += min(A+B+C,A+B+D,A+D+E,A+E+C,B+D+F,B+F+C,C+E+F,D+E+F) * 4
elif N == 1:
    ans = A+B+C+D+E+F-max(A,B,C,D,E,F)
print(ans)