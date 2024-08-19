import pandas as pd

"""
Desarrollar código en Python que extraiga los datos del archivo adjunto y calcule:

    El vector de IMC
    
    La media de los pesos y la media de las estaturas
    
    El ID de la persona de mayor peso, de la persona de menor estatura
    
    El vector de los ID de las personas con IMC>=28

Todos los resultados se ponen en una variable y se imprimen.
"""

df = pd.read_excel("./data/datosPE.xlsx", index_col=0)

#vector de imc
imc = df.Peso/df.Estatura**2
imc.name="imc"

print(df.join(imc))

#La media de los pesos y la media de las estaturas
medias = df.mean()
print("Medias\n    "+ "\n    ".join([f"{k}: {v:.2f}" for k, v in medias.items()]))


#El ID de la persona de mayor peso, de la persona de menor estatura
persona_mas_pesada = df["Peso"].idxmax()
print("Persona con mayor peso: ", persona_mas_pesada)
persona_menor_estatura = df["Estatura"].idxmin()
print("Persona con menor estatura", persona_menor_estatura)

#El vector de los ID de las personas con IMC>=28
id_imc_geq_28 = imc[imc>=28].index
print("Vector de los ID de personas con IMC >= 28", id_imc_geq_28.values)