# Codigo parcial 2

print("\nBienvenido al programa.\n")

n = 0
while n <= 0:

    n = int(input("Ingrese un numero con el cual desea calcular la serie -> "))
    if n <= 0:
        print("\nEl valor ingresado no puede ser negativo, por favor vuelva a intentarlo.\n")

operacion = 0
operacion2 = 0

for i in range(0,n):
    operacion = 1 + 1/(i+1) 
    operacion2 += 1/(i+1)
    print(f"\nEl resultado de la operacion es igual a: {operacion2} ")

print("\nFin del programa.\n")