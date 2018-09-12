import os
 
def menu():

	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opcin")
	print ("\t1 - primera opcin")
	print ("\t2 - segunda opcin")
	print ("\t3 - tercera opcin")
	print ("\t9 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opcin 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opcin 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		input("Has pulsado la opcin 3...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opcin correcta...\npulsa una tecla para continuar")