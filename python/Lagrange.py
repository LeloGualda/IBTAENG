

""" 
 metodo de jacobi || 
 
 matrizes esparta são matrizes com muitos zeros

criterio do metodo de jacobi 
  alf: 
    soma de todos menos a diagonal sobre a digonal  < 1

metodo de gauss-seidel

    criterio de gauss:
    
"""
def lagrange(vector):
    x = [1, 2, 3];
    for i in range(0, 1):
        for k,point in enumerate(vector):
            aux = [0,0]
            for j in range(0,len(x)-1):
                if(len(x)-1 < k+1):
                   aux[j] = x[(k+1)*-1]
                else:
                    aux[j] = x[k+1]
            print(aux)


""" 
print(k+1,len(x))        
 #x[k] = (vector[k]["y"] - (vector[k]["x1"] * x[1]) - (vector[k]["x2"] * x[2])) * (1 / vector[k]["x"+str(k)])

       n1 = (vector[0]["y"] - (vector[0]["x1"] * x[1]) - (vector[0]["x2"] * x[2])) * (1 / vector[0]["x0"])
        n2 = (vector[1]["y"] - (vector[1]["x0"] * x[0]) - (vector[1]["x2"] * x[2])) * (1 / vector[1]["x1"])
        n3 = (vector[2]["y"] - (vector[2]["x0"] * x[0]) - (vector[2]["x1"] * x[1])) * (1 / vector[2]["x2"])
        print(n1,n2,n3)
"""



