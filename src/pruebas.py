#!/usr/bin/python
#!encoding: UTF-8

import prct08

t_upla_intervalos=(10,100,1000,10000,100000)
t_upla_umbral=(0.0001,0.00001,0.000001,0.0002,0.0000001)
for i in t_upla_intervalos:
  print ('Con el número de intervalos %i ') %(i)
  for j in t_upla_umbral:
    resultado=prct08.error(i,1,j)
    print(' Prcentaje de error para el umbral %i es %f') %(j, resultado)