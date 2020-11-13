bandera = True
acum=0
while bandera:
    valor=int(input("Ingresa el valor a sumar: "))
    acum+=valor
    if(valor==99):
        bandera=False
print("Tu suma total es: " ,acum)