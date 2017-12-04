class raiz:
	def secantes (f, A, B):
		E = 1
		while (E!=0):
			D = f(A)
			E = f(B)
			C = (A*E-B*D)/(E-D)
			B = A
			C = B
		raiz = B
		return  raiz
