def getosinfo():
    import os

    current = os.getcwd()
    print("Current Path: ",current)
    newpath = os.chdir('/etc')
    envr = os.getenv('HOME')
    syst = os.uname()
    print("Sysname: ",syst[0])
    print("NodeName: ",syst[1])
    print("Machine: ",syst[4])
    print("Home Path: ",envr)
    current = os.getcwd()
    print("New Path: ",current)

def menu():
    import os
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print ("Selecciona una opción")
    print ("\t1 - Get OS Info")
    print ("\t2 - segunda opción")
    print ("\t3 - tercera opción")
    print ("\t0 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		getosinfo()
		input("\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		input("\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		input("\npulsa una tecla para continuar")
	elif opcionMenu=="0":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

def main():
    menu()
    

if __name__ == "__main__":
    main()