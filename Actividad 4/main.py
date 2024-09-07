import numpy as np

np.random.seed(42069)
"""
Genere una lista L con los resultados de emular 1000 veces el experimento de obtener la suma de dos dados. 
Suponga que los dados están cargados y el 5 tiene el doble de probabilidades que los demás. 
¿Qué porcentaje de los resultados fue 10?
"""

L = [np.random.choice([1,2,3,4,5,5,6],2).sum() for _ in range(1000)]
print(sum([l==10 for l in L])/1000)

"""
Genere una lista M con los resultados de emular las respuestas aleatorias de 1000 exámenes de 8 preguntas verdadero-falso.  
¿Cuál fue el promedio de calificación sobre 100?
"""

M = np.random.binomial(p=0.5,n=8, size=1000)/8
promedio=M.mean()
print(promedio/100)

""""
Se sabe que por un crucero pasan en promedio 20 coches por minuto. 
Emule aleatoriamente los resultados de tomar mediciones cada minuto durante una hora. 
¿Cuál fue el mayor y el menor valor obtenido?
"""

X=np.random.poisson(20,60)
print(X.min(), X.max())

"""
El coeficiente intelectual (IQ) es un estimador de la inteligencia general. 
Se distribuye normalmente con una media de 100 y desviación estándar de 15.  
Genere una lista Q que emule los IQ de una muestra aleatoria de 500 personas. 
Si se considera a una persona superdotada si su IQ es igual o mayor a 130, 
¿cuántos superdotados se obtuvieron en la simulación?
"""
Q=np.random.normal(scale=15,loc=100,size=500)
print((Q>=130).sum())
