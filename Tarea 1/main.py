import pandas as pd

"""
Primero lea la hoja vt en un Dataframe vt y sobre este:

    Suponga que ha habido un olvido y no se tomó en cuenta un Ingreso mensual de $1000 en todos los meses. Modifique el DataFrame para aumentar en $1000 los ingresos de cada mes.
    Agregue una columna Utilidad (Ingreso - Gasto).
    Encuentre el promedio de Gasto en los meses en los que la Utilidad fue negativa.
    Encuentre los ingresos totales del año.
    Encuentre la lista de los meses en los que la Utilidad fue positiva.
"""

df_vt = pd.read_excel("./data/datosCT.xlsx",sheet_name="vt")


#Modifique el DataFrame para aumentar en $1000 los ingresos de cada mes.
df_vt.Ingreso = df_vt.Ingreso+1000

#Agregue una columna Utilidad (Ingreso - Gasto).
df_vt["Utilidad"]=df_vt["Ingreso"]-df_vt["Gasto"]

#Encuentre el promedio de Gasto en los meses en los que la Utilidad fue negativa.
promedio_gasto_en_utilidad_negativa = df_vt[df_vt["Utilidad"]<0]["Gasto"].mean()

#Encuentre los ingresos totales del año.
ingresos_totales = df_vt["Ingreso"].sum()

#Encuentre la lista de los meses en los que la Utilidad fue positiva.
meses_con_utilidad_positiva = df_vt[df_vt["Utilidad"]>0].iloc[:,0].tolist()

print(f"\033[92mEjercicio 1 \n"
      f"    El promedio del gasto en los meses de utilidad negativa: {promedio_gasto_en_utilidad_negativa:,}\n"
      f"    Ingresos totales del año: {ingresos_totales:,}\n"
      f"    Meses con utilidad positiva: {", ".join(meses_con_utilidad_positiva)}\033[0m")

print(df_vt)

"""
Ahora lea la hoja 8c, que representa las distancias en kilómetros entre una serie de ciudades, en un Dataframe cd y sobre este:

    Convierta todos los valores a millas (km/1.609)
    Genere una serie llamada gdl con las distancias a partir de Guadalajara a todas las ciudades.
    Encuentre la lista de las ciudades que están a más de 1000 millas de Guadalajara.
"""

df_8c = pd.read_excel("./data/datosCT.xlsx",sheet_name="8c",index_col=0)

#Convierta todos los valores a millas (km/1.609)
df_8c = df_8c/1.609

#Genere una serie llamada gdl con las distancias a partir de Guadalajara a todas las ciudades.
gdl:pd.Series = df_8c.GDL
gdl.name = "gdl"

#Encuentre la lista de las ciudades que están a más de 1000 millas de Guadalajara.
ciudades_a_mas_de_1000_millas = gdl[gdl>1000].index.tolist()


print(f"\033[92mEjercicio 2 \n"
      f"    Ciudades a más de 1000 millas de Guadalajara: {", ".join(ciudades_a_mas_de_1000_millas)}\033[0m")

print(df_8c)
print(gdl)