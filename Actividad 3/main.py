import numpy as np

#Inicialice la semilla de aleatoriedad con un valor fijo arbitrario
np.random.seed(42069)

#Genere un arreglo G con los elementos {3,6,9,...,39}
G=np.arange(3,40,3)

#Imprima una permutación aleatoria de los elementos de G.
print(np.random.permutation(G))

#Obtenga una arreglo H con 4 elementos de G seleccionados de forma aleatoria (sin reemplazo).
H = np.random.choice(G,4,replace=False)

#Genere un arreglo L de 100 números aleatorios enteros en [5,100]
L=np.random.randint(5,101,100)

#Imprima la cantidad de números pares en L.
print(sum(L%2==0))

#Genere un arreglo M de 100 números aleatorios reales en [3,10)
M=np.random.uniform(3,10,100)

#Imprima la suma de los elementos de M que están en el intervalo [5,8]
print(sum(M[(M>=5)&(M<=8)]))
