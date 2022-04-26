def computeS(X,W):
	s=0
	S=[]
	for i in range(0,len(X)):
		for j in range(0,len(X[i])):
			s=s+(W[j]*X[i][j])
		S.append(s)
		s=0
	return S
def y_hat(S):
	Y_hat=[]
	for i in range(0,len(S)):
		if S[i]>0:
			Y_hat.append(1)
		elif S[i]<=0:
			Y_hat.append(-1)

	return Y_hat

def computeError(Y_hat,Y):
	count_e=0.0
	Error=0
	for i in range(0,len(Y)):
		if Y[i]!=Y_hat[i]:
			count_e=count_e+1
	Error=(count_e/len(Y))
	return Error

def learningRule(W,yi,Xaum):
	w=[]
	for i in range(0,len(W)):
		aux=W[i]+(yi*Xaum[i])
		w.append(aux)
	return w

def perceptron(Xaum,Y,Wo):
	W=Wo
	count=0
	error=computeError(y_hat(computeS(Xaum,W)),Y)
	print("| \t While\t     | \ti\t   |\t     Xi  \t   | \t yi_hat\t  | \tIs Yi_hat!=Yi     |\tW\t\t| ")
	eq="No"
	print("---------------------------------------------------------------------------------------------")
	print("Error = ",error)
	print("---------------------------------------------------------------------------------------------")
	while error!=0.0:
		for i in range(0,len(Xaum)):
			yiHat=y_hat(computeS([Xaum[i]],W))
			if yiHat[0]!=Y[i]:
				W=learningRule(W,Y[i],Xaum[i])
				eq="Yes"
			print("|\t."+str(count)+"\t.    | \t."+str(i)+"\t.  |\t.    ["+str(Xaum[i][1])+","+str(Xaum[i][2])+"]  \t.  | \t."+str(yiHat)+"\t. | \t"+eq+"\t\t   |\t."+str(W)+"\t|")
			eq="No"
		error=computeError(y_hat(computeS(Xaum,W)),Y)
		count=count+1
		print("---------------------------------------------------------------------------------------------")
		print("Error = ",error)
		print(y_hat(computeS(Xaum,W)))
		print("---------------------------------------------------------------------------------------------")


if __name__ == '__main__':
	Xaum=[[1,-4,7],[1,8,-8],[1,7,4]] 
	Y=[1,1,-1] 
	Wo=[1,-2,7] 
	perceptron(Xaum,Y,Wo) 