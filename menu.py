#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Get OS System information")
	print ("\t2 - List dir")
	print ("\t3 - Print only")
	print ("\t0 - salir")
 
 
