def esPrimo(num):
    if(num<2):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

gato=int(input("Ingresa hasta que numero quieres llegar: "))
bandera=True
c=0

while(bandera):
    c+=1
    if(esPrimo(c)):
        print(c, " es primo")
    if(c>=gato):
        bandera=False
