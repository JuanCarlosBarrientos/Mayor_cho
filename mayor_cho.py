#!/usr/bin/env python
#-*- coding: utf-8 -*-
num = int(raw_input('mete un numero positivo (si te aburres mete un negativo y terminas): '))
mayor = num
while num >=0:
	num = int(raw_input('mete un numero positivo (si te aburres mete un negativo y terminas): '))
	if num >mayor:
		mayor=num
	num = int(raw_input('mete un numero positivo (si te aburres mete un negativo y terminas): '))
if num<0:# si llega aqui no ha metido ni un numero positivo y num es un numero negativo
	print "Nos hemos aburrido pronto"
else:
	print "El mayor del chorro números es " + str(mayor)
