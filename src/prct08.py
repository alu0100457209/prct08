#!/usr/bin/python
#!encoding: UTF-8

import Ejer_Pi
import sys

#Sirve para sacar los porcentajes de error
def error (nro_intervalo, nro_test, umbral):
   fallo = 0

#El número de test
   for i in range(1, nro_test+1):
      a=Ejer_Pi.aproximacion_pi(nro_intervalo)
      if abs(a - Ejer_Pi.PI) > umbral:
        fallo = fallo + 1	
   return fallo * 100 / nro_test

if __name__=="__main__":
  
#Leemos los datos por pantalla  
  if len(sys.argv) == 4:    
    nro_intervalos = int(sys.argv[1])
    nro_test = int(sys.argv[2])
    umbral = float(sys.arg[3])
  else:
    print('No ha intruducido el numero de intervalos y el numero de veces en la linea de comandos, asi que, ahora van a ser pedidos por pantalla.')
    nro_intervalo = int(raw_input('El número de intervalos que desea aplicar: '))
    nro_test = int(raw_input('Introduce el número de veces que quieres que lo haga: '))
    umbral = float(raw_input('Introduce el error máximo que puede tener'))
  while nro_intervalo<=0:
    nro_intervalo = int(raw_input('El número de intervalos debe ser mayor que 0. Intruduce un numero de intervalos mayor que 0.'))
  while nro_test<=0:
    nro_test = int(raw_input('El número de veces debe ser mayor que 0. Intruduce un número de veces mayor que 0.'))
  while umbral<=0:
    umbral = float(raw_input('El número del error debe ser mayor que 0. Introduce un error mayor que 0'))
  
#Mostramos el porcentaje  
  print ('El porcentaje de errores es %i') %(b)