#!/usr/bin/python

import sys

PI = 3.1415926535897931159979634685441852

def aproximacion_pi(n):
  suma = 0.0
  for i in range(1, n+1):
    x_i = (i - 0.5) / float(n)
    fx_i = 4.0 / (1.0 + x_i * x_i)
    suma = suma + fx_i
  aproximacion = suma / float(n)
  return aproximacion

lista = []

if __name__=="__main__":
  if len(sys.argv) == 3:    
    n = int(sys.argv[1])
    veces = int(sys.argv[2])
  else:
    print('No ha intruducido el numero de intervalos y el numero de veces en la linea de comandos, asi que, ahora van a ser pedidos por pantalla.')
    n = int(raw_input('El numero de intervalos que desea aplicar: '))
    veces = int(raw_input('Intruduce el numero de veces que quieres que lo haga: '))
  while n<=0:
    n = int(raw_input('El numero de intervalos debe ser mayor que 0. Intruduce un numero de intervalos mayor que 0.'))
  while veces<=0:
    veces = int(raw_input('El numero de veces debe ser mayor que 0. Intruduce un numero de veces mayor que 0.'))

  for i in range(1,veces+1):
     a = i * n
     s = aproximacion_pi(a)
     lista = lista + [s]

  print ('  i      PI35DT       lista i      PI35DT - lista i')
  for i in range(veces):
     print ('%3i   %.10f   %.10f   %.10f') %(i+1, PI, lista[i], abs(PI-lista[i]))