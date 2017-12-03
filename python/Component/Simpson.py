def simpson(f,x0,x1,n):
    area = -f(x0)
    h = (x1-x0)/n
    for i in range(0,n+1):
        if(i%2):
            area += 4 * f(x0 + (h*i))
        else:
            area += 2 * f(x0 + (h*i))
    area = (area-f(x1))*h/3
    return area


def myfunction(x):
    return  (x*x) - x

'f(x)= x²-x  ∫ 2 a 3  | n = 4'
' resultado 23/6'

print(simpson(myfunction,2,3,4),23/6)
