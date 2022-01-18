class CuentaBancaria:
    relacion_cuentas=[]

    def __init__(self, tasa_interes=0.00, balance=0):
        self.tasa_interes=tasa_interes
        self.balance=balance
        CuentaBancaria.relacion_cuentas.append(self)

    def deposito(self,monto):
        self.balance+=monto
        return self
    
    def retiro(self,monto):
        self.balance-=monto
        return self
    
    def mostrar_info_cuentas(self):
        print(f"Balance: ${self.balance}, Tasa de interés: {self.tasa_interes}")
    
    def generar_interes(self):
        if self.balance>0:
            self.balance=self.balance*(1+self.tasa_interes)
            return self
        else:
            print("Saldo negativo, no es posible generar interés")
            return self

    @classmethod
    def info_cuentas(cls):
        for i in range(0,len(CuentaBancaria.relacion_cuentas)):
            CuentaBancaria.mostrar_info_cuentas(CuentaBancaria.relacion_cuentas[i])

    

