def printMat(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print("%5g"%mat[i][j])
        print()
    print()


A = [
[1,1,1],
       [4,2,1],
       [9,3,1]
    ]
B = [5,7,9]
n = len(A)
x = [0]*3
x[n-1] = B[n-1]/A[n-1][n-1]

for i in range(1,n):
    for k in range(i,n):
        m = A[k][i-1]/A[i-1][i-1]
        B[k] = B[k] - m*B[i-1]
        print(m)
        for j in range(i-1,n):
            A[k][j] = A[k][j] - (m*A[i-1][j])
        #   print(A)

for i in reversed(range(0,n)):
    soma = 0
    for j in range(i+1,n):
        soma = soma + A[i][j]*x[j]
    x[i] = (B[i] - soma)/A[i][i]


print(x)
