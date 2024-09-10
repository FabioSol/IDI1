import numpy as np
from matplotlib import pyplot as plt
np.random.seed(420696969)
"""
1.- En el juego Calabozos y dragones se usan dados no cúbicos.
Suponga que tiene dados en forma de octaedro cuyas caras marcan 1,2,2,3,4,6,10,12.
Emule el experimento de obtener la suma de dos de esos dados, genere una lista aleatoria L con los resultados de
1000 lanzamientos. Imprima el resultado que más se obtuvo en el experimento y el que menos.
"""

L = np.random.choice([1,2,2,3,4,6,10,12], size=(1000,2)).sum(axis=1)
print("mas obtenido:%s menos obtenido:%s"%(lambda x,y: (x[y.argmax()],x[y.argmin()]))(*np.unique(L,return_counts=True)))

"""
2.- Suponga que tiene una baraja que tiene las cartas numeradas del 1 al 10 de cuatro colores distintos 
(azul, rojo, verde y amarillo), es decir, 40 cartas en total. Emule el proceso de repartir 5 cartas a un jugador. 
Repita el proceso 5000 veces e imprima según este experimento, 
¿qué tan probable es obtener un juego que sume más de 30 puntos?
"""
deck = np.array([[i]*4 for i in range(1,11)]).reshape((40,))
games =np.array([np.random.choice(deck,replace=False,size=5) for _ in range(5000)])
print("la probabilidad de obtener un juego que sume más de 30 puntos es: %s"%((games.sum(axis=1)>30).sum()/5000))

"""
3.- Emule el evento de contestar un examen de 12 preguntas, cada una de 4 opciones (sólo una correcta). 
Entregue una lista M con las calificaciones (sobre 100) de 500 exámenes contestados aleatoriamente.
"""

M = np.random.binomial(12,1/4,size=500)/12*100

""""
4.- Se sabe que durante un turno de una fábrica se producen 10 pelotas cada minuto en promedio. 
Emule aleatoriamente los resultados de tomar mediciones cada minuto durante una hora específica del día. 
Ahora cree una lista N con el promedio diario de los resultados emulados de hacer las mediciones durante 30 días. 
Calcule la desviación estándar de los promedios diarios.
"""

N=np.random.poisson(lam=10,size=(30,60)).mean(axis=1)
print(f"desviación estandar de los promedios diarios{N.std()}")
"""
5.- Si sabemos que las estaturas de cierta población se distribuyen de forma normal con una media de 1.68 m y una 
desviación estándar de 0.14 m. Genere una lista aleatoria Q para emular una muestra de 500 personas. 
¿Cuál es la estatura promedio de la muestra? ¿Cuál fue la menor y la mayor estatura obtenida?
"""
Q=np.random.normal(loc=1.68,scale=0.14,size=500)

print("estatura promedio:%s menor:%s mayor:%s"%(Q.mean(),Q.min(),Q.max()))
""""
6.- Los valores del largo de barras de metal en una fábrica están entre 80 y 90 cm. 
El valor esperado del largo de una barra es de 83 cm y se sabe que las probabilidades a partir de este valor a 
los extremos decrecen linealmente. Genere un histograma con 10 clases a partir de la emulación de una 
muestra aleatoria de 10,000 barras.
"""

plt.hist(np.random.triangular(80,83,90,10_000),bins=10)
plt.title('Histograma de distribución triangular')
plt.xlabel('Longitud de la barra')
plt.ylabel('Frecuencia')
plt.show()

"""
7.- Para hacer una comparación entre la distribución exponencial y la distribución gamma, 
genere una lista de 10000 muestras exponenciales con media 10, y otra con 10000 muestras gamma con α =2 y β=1/5. 
Dibuje los histogramas de ambas en la misma gráfica y el mismo número de barras. ¿Qué observa?
"""
bins=[i for i in range(60)]
plt.figure()
plt.hist(np.random.exponential(10,10_000),bins=bins,alpha=0.6)
plt.hist(np.random.gamma(2,5,10_000),bins=bins,alpha=0.6)
plt.title('Comparación entre la distribución exponencial y la gamma')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

"""
observación: las frecuencias cercanas a 10 son mayores en la distribución gamma que en la exponencial, 
mientras que las más lejanas a 10 son mayores para la exponencial. esto es porque la media es la misma para ambas distribuciones
pero la varianza para la gamma es 2/(1/25)=50 y para la exponencial 1/(1/10^2)=100 lo que significa que los valores de la gamma están más centrados.
"""