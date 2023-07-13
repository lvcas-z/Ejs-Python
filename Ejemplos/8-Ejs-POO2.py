class Cuenta :
    def __init__(self,nombre,apellido,nroCuenta,saldo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nroCuenta = nroCuenta
        self.__saldo = saldo
    
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getNroCuenta(self):
        return self.__nroCuenta
    def getSaldo(self):
        return self.__saldo
    
    def __str__(self):
        return f"Nombre Completo : {self.getNombre()} {self.getApellido()} || Numero de Cuenta : {self.getNroCuenta()} || Saldo : {self.getSaldo()}"
    

alex = Cuenta("Alex","Rodriguez","000231230322",35000)

print(alex)