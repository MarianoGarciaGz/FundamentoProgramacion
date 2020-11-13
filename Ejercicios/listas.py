texto="hola"
entero=1
decimal=3.5
booleano=True

lista=[1,"hola",3.5,True]
lista.append("adios")
lista.remove("hola")
lista.append("adios")

print("'adios' se repite: " ,lista.count("adios"))
print(lista)
lista.reverse()
print(lista)
print(len(lista))

print(type(texto))
print(type(entero))
print(type(decimal))
print(type(booleano))

if texto is type(str):
    print("bien hecho")

"""
acum=0
for i in lista:
    acum+=i
print(acum)

"""

