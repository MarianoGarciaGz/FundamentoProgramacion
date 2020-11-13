#Sumar números ingresados hasta que se ingrese el 99, sumar los anteriores y el 99

def agregarSuma(num):
    if(num!=99):
        lista.append(n)
        return False
    if(num==99):
        lista.append(n)
        return True

lista = []
bandera=True
print("Con el número 99 se genera la respuesta")

while(bandera):
    n=int(input("Ingresa el numero que quieres sumar: "))
    if(agregarSuma(n)):
        bandera=True
    if(n==99):
        bandera=False

suma=0
x=0

while x<len(lista):
    suma=suma+lista[x]
    x=x+1
print("La suma de todos tus numeros ingresados es " ,suma)