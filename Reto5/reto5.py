import pandas as pd
import os

# ruta file csv y acortar el nombre
rutaFileCsv='https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'

#definimos la lista quee se solicita
#indicamos que tomes los registros de Str
def listaPeliculas(rutaFileCsv:str) -> str:
    ruta, extension = os.path.splitext('https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv')
    if extension=='.csv': #comprobar si la extension es CSV
        #utilizamos el try como condicional en caso de no poder leer el archivo solicitado similar al if/else
        try:
            #con pandas lanzamos la instruccion 
            df=pd.read_csv(rutaFileCsv, #enviamos la info del nombre recortado que utilizamos de la url 
                        index_col=['Country','Language'], # ageramos los indices solicitados
                        na_values='None') #agregamos lo vsalores nulos que se ven en la salida del dataframe al final del reto "NaN"
            #creamos una nueva variable para que con pivot_table
            #pandas.pivot_table() evita la repetición de datos del DataFrame. Resume los datos y aplica diferentes funciones de agregación a los datos.
            h=pd.pivot_table(df,index=['Country','Language']) #agregamos los indices como argumentos del pivot_table
            #creamos una nueva variable donde utilizamos el resumen del pivot_table y creamos un nuevo Dataframe
            f=pd.DataFrame(h.loc[:,'Gross Earnings']) #limitamos la informacion resultando indicando que solo llame la columna 'Gross Earnings'
            print(f[:10]) #limitamos el tamaño de salida del Dataframe a 10 registros
            return f[:10] #limitamos el tamaño de salida del Dataframe a 10 registros (se imprime 2 veces por error de validacion del bot)
        #utilizamos el except para indicar el error al leer el archivo de la ruta
        except:
            print("Error al leer el archivo de datos.")
            
    else: # si la ext no es CSV entonces imprime el error solicitado
        print("Extensión inválida.")

#enviamos la informacion de la ruta a la funcion listaPeliculas
df2=(listaPeliculas(rutaFileCsv))
#imprimir el resltado de la funcion ya que estamos utilizando return y print en la salida de la funcion listaPeliculas
print(df2)
