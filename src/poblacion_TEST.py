# -*- coding: utf-8 -*-
'''
Created on 12 oct. 2018
@author: Toñi Reina
REVISOR: José Antonio Troyano, Daniel Mateos, Mariano González
ÚLTIMA MODIFICACIÓN: 17/10/2018

Programa Test

'''

from poblacion_SOLUCION import *
 
################################################################
# Funciones auxiliares
# Permite mostrar por pantalla la colección 
################################################################

def mostrar_numerado(coleccion, cuantos):
    
    i=0
    # Se recorre la colección y se muestra la tupla (fila) 
    for tupla in coleccion:
        
        i=i+1
        
        # Se muestra por pantalla el orden y la tupla
        if i <= cuantos:
           print (i, tupla) 
          
        if i == (cuantos):
           print ('\nNOTA: Solo se han mostrado', cuantos, 'registros\n' ) 

################################################################
# TESTEO A REALIZAR
################################################################

# Test de la función lee_poblaciones
def test_lee_poblaciones():
    print("\nLeidos " , len (POBLACIONES), "registros con información de la población mundial\n")
    # Mostramos solo 50 filas
    mostrar_numerado(POBLACIONES, 50)    

# Test de la función calcula_paises
def test_calcula_paises():         
    paises = calcula_paises(POBLACIONES)
    print("Paises distintos leidos ", len (paises), "\n")
    
    # Mostramos solo 100 paises
    mostrar_numerado(paises, 100)

# Test de la función filtra_por_pais
def test_filtra_por_pais():         
    poblacion_es = filtra_por_pais(POBLACIONES, "Spain")
    print("Poblacion españa")
    print("Leidos " , len (poblacion_es), "datos de población de España")
    
    # mostramos solo 50 
    mostrar_numerado(poblacion_es, 50)

def test_filtra_por_paises_y_anyo():         # Test de la filtra_por_pais
    paises= ["Spain","Portugal","France","Mexico","China"]
    poblacion_2016 = filtra_por_paises_y_anyo(POBLACIONES, 2016, paises)
    print("Leidos " , len (poblacion_2016), "datos del año 2016 para los paises", paises)
    mostrar_numerado(poblacion_2016, 300)

def test_muestra_evolucion_poblacion():
    muestra_evolucion_poblacion(POBLACIONES, "Spain")

def test_muestra_comparativa_paises_anyo():
    muestra_comparativa_paises_anyo(POBLACIONES, 2016, ["Spain","Portugal","France","Mexico","China"])
        
################################################################
#  Programa principal
################################################################

# Se le pasa el fichero .csv  
POBLACIONES = lee_poblaciones('./data/population.csv')
 
#test_lee_poblaciones()
#test_calcula_paises()

# test_filtra_por_pais()
# test_filtra_por_paises_y_anyo()
test_muestra_evolucion_poblacion()
#test_muestra_comparativa_paises_anyo()
