import numpy as np

A = np.array([3,5,7,11]).reshape((2,2))

B = np.matrix([[-2,4],
               [9,10]])

I = np.identity(2)

C = 3*A+B-I

D = np.concatenate((A,B),axis=1)
print("Imprima la suma de los elementos de D ",D.sum())
print("La cantidad de números pares que tiene: ",(D%2==0).sum())

F = np.arange(1,101).reshape((10,10),order='F')
print("Imprima la suma de los valores de F cuyos valores estén en el intervalo [10,20]: ",F[(F>=10)&(F<=20)].sum())