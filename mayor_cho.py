#!/usr/bin/env python
#-*- coding: utf-8 -*-
mayor = 0
aburrido = False
while num >=0:
	num = int(raw_input('mete un numero positivo (si te aburres mete un negativo y terminas): '))
	if num < 0:
		aburrido = True
	elif num > mayor:
		mayor = num

print "El mayor del chorro números es " + str(mayor)
		


