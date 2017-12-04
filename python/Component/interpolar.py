import math

class Interpolar:
   dom = []
   img = []
   polinomio = []
   def Escalonamento(self):
       matrix = list(self.matriz())
       resultante = list(self.img)

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

       self.polinomio = x
       return x

   def F(self,x):
       vetor = list(self.polinomio)
       soma = vetor[-1]
       for i in reversed(range(1,len(vetor))):
           soma += vetor[-i -1] * math.pow(x,i)
       return soma

   def addPoint(self,x,y):
       self.dom.append(x)
       self.img.append(y)
       self.matriz()
       self.Escalonamento()

   def matriz(self):
       matriz = [0]*len(self.dom)
       for i,v in enumerate(self.dom):
           matriz[i] = [0] * (len(self.dom))
           for j in reversed(range(0,len(self.dom))):
               matriz[i][len(self.dom)-j-1] = math.pow(v,j)
       return matriz
"""" 
A = [
       [1,1,1],
       [4,2,1],
       [9,3,1]
]
B = [5,7,9]
"""


myf = Interpolar()
myf.addPoint(1,5)
myf.addPoint(2,7)
myf.addPoint(3,9)
print(myf.polinomio)
print(myf.F(4))
