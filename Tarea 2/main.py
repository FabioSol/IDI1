import numpy as np

#Genere una lista L con los primeros 50 números naturales impares
L = list(range(1,50,2))

#Convierta la lista L en un arreglo A
A=np.array(L)

#Imprima el 7mo número de A, los elementos en las posiciones 3 a 9 y los últimos 3 en orden descendente.
print(A[6],A[3:9],A[-3:])

#Genere un arreglo B con enteros iniciando en 20 descendiendo en 3 hasta el 5
B=np.arange(20,5,-3)

#Invierta el arreglo B y guárdelo en C (use Slicing)
C=B[::-1]

#Genere un arreglo D con 100 puntos igualmente espaciados desde el 2 hasta el 30
D,d_step=np.linspace(2,30,100,retstep=True)

#Imprima el tamaño de paso usado para generar D
print(d_step)

#Genere un arreglo E de 100 puntos igualmente espaciados de 5 a 100 guardados como enteros.
E=np.linspace(5,100,100,dtype=int)

#Genere un arreglo I con los elementos de A que son múltiplos de 3
I=A[A%3==0]

#Genere una matriz F de 10x10 a partir de los elementos de D tomados por filas.
F=D.reshape((10,10))

#Genere una matriz G de 10x10 a partir de los elementos de E tomados por columnas.
G=E.reshape((10,10),order='F')

#Genere la submatriz M de G con los elementos de sus filas 1 y 2 y columnas de la 3 a la 6.
M=G[[1,2],3:6]

#Obtenga la matriz N a partir de los elementos de G elevados al cuadrado menos 3
N=G**2-3

#Imprima SI en caso de que la matriz N contenga algún múltiplo de 17 y NO en caso contrario.
print("SI" if ((N%17)==0).any() else "NO")

#Imprima la tercer fila de F y la cuarta columna de G
print(F[2],G[:,3])

#Defina la matriz H como la suma de F y G
H=F+G

#Obtenga un arreglo J con los elementos de H que están en el intervalo (20,30)
J=H[(H>20)&(H<30)].flatten()

#Cambie los elementos de H menores de 30 por cero, guarde la matriz resultante en K.
K:np.ndarray=np.vectorize(lambda x: 0 if x<30 else x)(H)

#Imprima la cantidad de columnas de K cuya suma es más de 500.
print(sum(np.apply_along_axis(sum,axis=0,arr=K)>500))

#Genere un arreglo Z con los promedios de cada columna de K
Z=np.apply_along_axis(np.mean,axis=0,arr=K)