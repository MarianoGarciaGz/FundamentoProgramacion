bandera=True
suma = 0
contador = 0

while(bandera):
    calif=int(input("Ingresa tu calificación: "))
    suma=suma+calif
    contador=contador+1
    s=int(input("Ingresar otra calificación? "))
    if(s==1):
        bandera=True
    else:
        bandera=False

prom=suma/contador

print("Tu promedio es de: " ,prom)