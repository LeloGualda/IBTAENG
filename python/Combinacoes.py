import math

class Combinacoes:
    def possibilidades(n, v, k, m, s, d, state, c):
        for i in range(k + d, len(v)):
            s[m] = v[i]
            if n - 1 == m:
                state.append(tuple(s))
            else:
                state = Combinacoes.possibilidades(n, v, i, m + 1, s, 1, state, c)
                continue
        return state
    def combinar(vetor):
        x = []
        for i in range(1,len(vetor)+1):
         (Combinacoes.possibilidades(i, vetor, 0, 0, i * [0], 0, x, 0))
        return x

#x = Combinacoes.combinar(VETOR)
#print("\n Quantidade da lista \t",len(x))
#print(" valor de 2^n -1 \t\t",2**len(VETOR)-1)

