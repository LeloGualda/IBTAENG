import math

def Escalonamento(matrix,resultante):
    n = len(matrix)
    x = [0]*len(resultante)
    x[n-1] = resultante[n-1]/matrix[n-1][n-1]

    for i in range(1,n):
        for k in range(i,n):
            m = matrix[k][i-1]/matrix[i-1][i-1]
            resultante[k]  = resultante[k] - m*resultante[i-1]
            for j in range(i-1,n):
                matrix[k][j] = matrix[k][j] - (m*matrix[i-1][j])

    for i in reversed(range(0,n-1)):
        soma = 0
        for j in range(i+1,n):
            soma = soma + matrix[i][j]*x[j]
        x[i] = (resultante[i] -soma)/matrix[i][i]

    return x

def Polinomios (vetor):
    soma = 0
    for i,v in enumerate(vetor):
        soma += math.pow(v,i+1)
    return soma
A = [
        [1,0,0],
        [0,2,2],
        [0,0,1]
    ]
B = [1,8,1]

print(Escalonamento(A,B))
