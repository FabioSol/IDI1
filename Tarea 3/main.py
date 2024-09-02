import numpy as np

np.random.seed(4206969)
#Genere una matriz Q de 5x5 con elementos aleatorios reales en [1,10)
Q=np.random.uniform(1,10,(5,5))

#Imprima el porcentaje de elementos de la matriz Q que están por encima del promedio.
print((Q>Q.mean()).sum()/Q.size)

#Genere una matriz L de 15x100 números reales en [0,8)
L=np.random.uniform(0,8,(15,100))

#Genere un arreglo M con los promedios de cada una de las 15 filas de L, luego imprima el promedio de los promedios.
M = np.apply_along_axis(np.mean,axis=1,arr=L)
print(np.mean(M))

#Emule el experimento de obtener la suma de dos dados y genere un arreglo aleatorio D con los resultados de 1000 lanzamientos
#(note que no todos los resultados son igual de probables).
D = np.fromiter((sum(np.random.randint(1,6,2)) for _ in range(100)),int)

#Suponga que tiene una caja con dos canicas rojas, tres azules y 5 blancas. Quiere emular el proceso de sacar 3 canicas de la caja de forma que no se regresa la canica que ya se sacó.
#Cree un arreglo C con los resultados de 10 experimentos
#(es decir, una lista de 10 listas con 3 elementos).
C= np.array([sum([{k:v for k,v in zip(["r","a","b"],np.identity(3))}.get(i) for i in np.random.choice(["r"]*2+["a"]*3+["b"]*5,size=3, replace=False)]) for _ in range(10)])