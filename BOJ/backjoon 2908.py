A,B = input().split(' ')
A = list(A)
B = list(B)
A.reverse()
B.reverse()
a = 0
b = 0
for i in range(len(A)):
    a = a + int(A[i])*(10**(len(A)-i-1))
for i in range(len(B)):
    b = b + int(B[i])*(10**(len(B)-i-1))  
print(max(a,b))  