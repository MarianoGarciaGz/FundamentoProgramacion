# Recibir un numero natural e imprimir todos los números primos que hay dentro de ese numero

numero = int(input("Ingresa hasta que número quieres saber sus numeros primos: "))
x = 0

if (numero > 1):
    for n in range(0, numero):
        for x in range(2, n):
            if (n % x == 0):
                break
        else:
            print(n, "es primo")

else:
    print("Tu número no es natural, intentalo de nuevo")
