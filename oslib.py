def getosinfo():
    import os

    syst = os.uname()
    print("Sysname: ",syst[0])
    print("NodeName: ",syst[1])
    print("Machine: ",syst[4])

def main():
    getosinfo()

if __name__ == "__main__":
    main()