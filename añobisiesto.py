#coding: utf8
def esbisiesto(anio):
	if (anio % 4 == 0 and anio % 100 != 0 )or anio % 400 == 0:
		print "es bisiesto"
	else :
		print "no es bisiesto"

esbisiesto(2100)
esbisiesto(2300)
esbisiesto(1955)
