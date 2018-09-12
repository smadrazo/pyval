import os
from menu import menu


def getosinfo():

    current = os.getcwd()
    print("Current Path: ",current)
    os.chdir('/etc')
    envr = os.getenv('HOME')
    syst = os.uname()
    print("Sysname: ",syst[0])
    print("NodeName: ",syst[1])
    print("Machine: ",syst[4])
    print("Home Path: ",envr)
    current = os.getcwd()
    print("New Path: ",current)

def listdir():
    dir = os.listdir('/Users/smadrazo')
    for file in dir:
        print(file)

while True:
	# Mostramos el menu
    menu()
	# solicituamos una opci0n al usuario
    opcionMenu = input("inserta un numero valor >> ")
 
    if opcionMenu=="1":
    	getosinfo()
    	input("\npulsa una tecla para continuar")
    elif opcionMenu=="2":
    	listdir()
    	input("\npulsa una tecla para continuar")
    elif opcionMenu=="3":
    	print ("")
    	input("\npulsa una tecla para continuar")
    elif opcionMenu=="0":
    	break
    else:
    	print ("")
    	input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")

def main():
    menu()
    

if __name__ == "__main__":
    main()