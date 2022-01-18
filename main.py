from CuentaBancaria import CuentaBancaria

cuenta1=CuentaBancaria(0.10)
cuenta2=CuentaBancaria(0.25)

cuenta1.deposito(100).deposito(200).deposito(300).retiro(50).generar_interes().mostrar_info_cuentas()
cuenta2.deposito(1000).deposito(200).retiro(500).retiro(600).retiro(150).retiro(200).generar_interes().mostrar_info_cuentas()

CuentaBancaria.info_cuentas()