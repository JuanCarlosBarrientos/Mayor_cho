#!/usr/bin/env python
#-*- coding: utf-8 -*-
mayor = 1
aburrido = False
while not aburrido:
	num = int(raw_input('mete un numero positivo (si te aburres mete un negativo y terminas): '))
	if num < 1:
		aburrido = True
	if num > mayor:
		mayor = num

print "El mayor del chorro números es " + str(mayor)
		


