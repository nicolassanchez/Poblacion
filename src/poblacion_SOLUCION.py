# -*- coding: utf-8 -*-

''' 
Poblacion mundial

@author: Toñi Reina
REVISOR: José Antonio Troyano, Daniel Mateos, Mariano González
ÚLTIMA MODIFICACIÓN: 07/10/2019

En este proyecto trabajaremos con datos de población mundial, representados mediante listas. 
Implementaremos una serie de funciones que nos permitirán mostrar gráficas de evolución de 
la población, así como, comparar la población en distintos países.

CONJUNTOS DE DATOS:
-------------------
El proyecto incluye un conjuntos de datos de prueba:
  - population.csv: con los datos de población de diversos paises o agrupaciones de paises 
    en distintos años.
 
FUNCIONES QUE FORMAN PARTE DEL EJERCICIO:
-----------------------------------------
- lee_poblaciones(fichero):
    lee el fichero de entrada y devuelve una lista de tuplas 
    (nombre_pais, cod_pais, anyo, num_habitantes)

- calcula_paises(poblaciones):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) 
    y devuelve una lista ordenada con los nombres
    de los paises o conjuntos de paises para los que hay datos

- filtra_por_pais(poblaciones, pais):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    devuelve una lista de tuplas (anyo, num_habitantes)
    con los datos del pais que se pasa como parámetro. 
    El pais se puede dar con su nombre completo o con su código

- filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    devuelve una lista de tuplas (nombre_pais, num_habitantes)
    con los datos del año pasado como parámetro para los paises 
    incluidos en el parámetro paises. 

- muestra_evolucion_poblacion(poblaciones, pais):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) 
    y genera un gráfico con la evolución de la población
    del pais dado como parámetro. El pais se puede dar con su nombre completo o con
    su código

- muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes), un año y 
    un grupo de paises y genera un gráfico 
    de barras con la población de esos países en el año dado como parámetro

'''
import csv
from matplotlib import pyplot as plt
from collections import namedtuple

Registro = namedtuple('Registro', 'nombre, codigo, año, censo')

########################################################################################
#  Lee el fichero de entrada y devuelve una lista de tuplas poblaciones
'''   
    ENTRADA: 
       - fichero: nombre del fichero de entrada -> str
    SALIDA: 
       - lista de tuplas (nombre, código, año, censo) -> [(str, str, int, int)]

    Cada línea del fichero se corresponde con los datos de un pais,  
    y se representa con una tupla con los siguientes valores:
        - Nombre del pais
        - Código del pais
        - Año 
        - Número de habitantes del pais (en ese año)

    NOTA: Hay que transformar la entrada (cadenas de caracteres) en valores numéricos
    en aquellos datos que sean de tipo numérico.
'''
########################################################################################

def lee_poblaciones2(fichero):

    # Lista de tuplas
    poblaciones = []

    with open(fichero, encoding='utf-8') as f:

        for linea in f:

            # Separamos la línea en cuatro usando ',' como delimitador
            nombre_pais, cod_pais, anyo, num_habitantes = linea.split(',')
            
            # Transformamos los valores str a int             
            anyo = int(anyo)
            num_habitantes = int(num_habitantes)
            
            # Añadimos las tuplas una a una
            poblaciones.append(( nombre_pais, cod_pais, anyo, num_habitantes))
    
    return poblaciones ## Se devuelve la lista de tuplas

############################################################################################
# Lee el fichero de entrada y devuelve una lista de tuplas poblaciones
# Otra forma de hacerlo
'''     
    ENTRADA: 
       - fichero: nombre del fichero de entrada -> str
    SALIDA: 
       - lista de tuplas (nombre, código, año, censo) -> [(str, str, int, int)]

    Cada línea del fichero se corresponde con los datos de un pais o agrupación de países, 
    y se representa con una tupla con los siguientes valores:
        - Nombre del pais
        - Código del pais
        - Año 
        - Número de habitantes del pais (en ese año)

    NOTA: Hay que transformar la entrada (cadenas de caracteres) en valores numéricos
    en aquellos datos que sean de tipo numérico.
'''
############################################################################################

def lee_poblaciones(fichero):

    # Lista de tuplas
    poblaciones = []

    with open(fichero, encoding='utf-8') as f:

        # Se crea un objeto lector (un iterator) que separará los valores por comas 
        lector = csv.reader(f)

        # Lista por comprensión sobre el objeto lector
        poblaciones = [(nombre_pais, cod_pais, int(anyo), int(num_habitantes)) 
                         for nombre_pais, cod_pais, anyo, num_habitantes in lector]

    return poblaciones ## Se devuelve la lista de tuplas

############################################################################################
# Calcular el conjunto de paises presentes en una lista de paises
'''
    ENTRADA: 
       - poblaciones: lista de tuplas (nombre, código, año, censo) -> [(str, str, int, int)]
    SALIDA: 
       - lista de paises -> [str]

    Toma como entrada una lista de tuplas (pais, cod_pais, anyo, num_habitantes) y 
    produce como  salida una lista ordenada con los nombres de los paises 
    para los que haya al menos un dato de poblacion. 
    La lista de salida no contendrá elementos repetidos.
'''
############################################################################################

def calcula_paises(poblaciones):
   
    # Obtenemos el conjunto de paises presentes
    s_paises = set(nombre_pais for nombre_pais, _, _, _ in poblaciones)
    # s_paises = {Chat, 'European Union', ...}

    # Convertimos el conjunto en lista para poder ordenarlo
    l_paises = list(s_paises)
    # l_paises = [Chat, 'European Union', ...]

    # Ordenamos los paises
    l_paises.sort()

    return l_paises # Se devuelve la lista de paises ordenados

##############################################################################################
# Selecciona las tuplas correspondientes a un determinado pais
'''    
    ENTRADA: 
       - poblaciones: lista de tuplas (nombre, código, año, censo) -> [(str, str, int, int)]
       - pais: del que se seleccionarán los registros -> str
    SALIDA: 
       - lista de tuplas (año, censo) seleccionadas -> [(int, int)]

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y
    produce como salida otra lista de tuplas (anyo, num_habitantes) con los datos de 
    poblacion del pais que se pasa como parámetro. El pais se puede indicar 
    bien dando su nombre completo, bien dando su código.
'''
############################################################################################## 

def filtra_por_pais(poblaciones, pais):
    
    reg_filtrados = []

    reg_filtrados = [(anyo, num_habitantes) 
                   for nombre_pais, cod_pais, anyo, num_habitantes in poblaciones 
                        if nombre_pais == pais or cod_pais == pais
                ]
    
    return reg_filtrados # Se devuelven los registros filtrados

##############################################################################################
# Selecciona las tuplas correspondientes a un conjunto de paises de un año concreto
'''  
    ENTRADA: 
       - poblaciones: lista de tuplas (nombre, código, año, censo) -> [(str, str, int, int)]
       - anyo: del que se seleccionarán los registros -> int
       - paises: de los que se seleccionarán los registros -> [str]
    SALIDA: 
       - lista de tuplas (pais, censo) seleccionadas -> [(str, int)]

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    produce como salida otra lista de tuplas (nombre_pais, num_habitantes) 
    en la que solo se incluyen aquellos datos correspondientes al año dado como parámetro 
    y de los paises incluidos en la colección paises
'''
############################################################################################## 

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):

    reg_filtrados = []

    reg_filtrados = [(nombre_pais, num_habitantes) 
                   for nombre_pais, _, an, num_habitantes in poblaciones 
                        if anyo == an and nombre_pais in paises]
 
    return reg_filtrados # Se devuelven los registros filtrados

##############################################################################################
# Genera una curva con la evolución de la población de un país. El pais puede
# darse como su nombre completo o por su código.
'''   
    ENTRADA: 
       - poblaciones: lista de tuplas (nombre, código, año, censo) -> [(str, str, int, int)]
       - pais: del que se generará la gráfica -> str
    SALIDA EN PANTALLA: 
       - diagrama con la evolución del censo del país

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    produce como salida un gráfico con la evolución de la población del país dado como
    parámetro a lo largo del tiempo. 
    
    Estas son las instrucciones 'matplotlib' para trazar el gráfico a partir una cadena con 
    el título que se va a mostrar en el gráfico, una lista de años y otra lista con los número
    de habitantes (con el mismo orden):
    
        plt.title(titulo)
        plt.plot(l_anyos,l_habitantes)
        plt.show()
'''
###############################################################################################
 
def muestra_evolucion_poblacion(poblaciones, pais):
    
    # Calculamos la lista de con los datos de población del pais dado 
    poblaciones_filtradas = filtra_por_pais(poblaciones, pais)
    
    l_habitantes = [num_habitantes for _, num_habitantes in poblaciones_filtradas]
    
    l_anyos = [anyo for anyo,_ in poblaciones_filtradas]
    
    # Componemos y visualizamos la gráfica
    titulo='Evolución de la poblacion de '+ pais
    plt.title(titulo)
    plt.plot(l_anyos,l_habitantes)
    
    plt.show()
   
###############################################################################################
# Genera una gráfica de barras en la que se muestra la comparativa de
# la población de varios países en un año concreto
'''    
    ENTRADA: 
       - poblaciones: lista de tuplas (nombre, código, año, censo) -> [(str, str, int, int)]
       - anyo: del que se generará la gráfica -> int
       - paises: de los que se generará la gráfica -> [str]
    SALIDA EN PANTALLA: 
       - diagrama de barras con la comparativa del censo por paises

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    produce como salida un gráfico de barras con el número de habitantes de los paises 
    dados como parámetro en el año anyo.
    Cada barra corresponde a un pais.
    
    Estas son las instrucciones 'matplotlib' para trazar el diagrama de barras
    a partir de una cadena con el título del gráfico, 
    una lista de nombres paises y otra lista (con el mismo orden) de
    número de habitantes de esos países:
       
        plt.title(titulo)
        indice = range(len(l_paises))
        plt.bar(indice, l_habitantes)
        plt.xticks(indice, l_paises, fontsize=8)
        plt.show()
    '''
###############################################################################################

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    
    # Calculamos la lista de poblaciones del año dado para los paises de la lista
    poblaciones_filtradas = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    
    l_habitantes = [num_habitantes for _,num_habitantes in poblaciones_filtradas]
    l_paises = [nombre_pais for nombre_pais,_ in poblaciones_filtradas]
  
    titulo = 'Población en el año ' + str(anyo)
    plt.title(titulo)
    indice = range(len(l_paises))
    plt.bar(indice, l_habitantes)
    plt.xticks(indice, l_paises, fontsize=8)

    plt.show()