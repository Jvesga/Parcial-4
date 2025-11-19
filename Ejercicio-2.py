#Crear una matriz 5x5. A continuacion, pesir un entero y una posicion de la matriz y sustituir el entero situado en la posicion nueva intruducida, mostrar la matriz.

matrizP = []
entero = int(input("Digite un valor entero: "))
filas= 5
columnas= 5

for i in range (filas):
    matrizP.append([])
    for j in range(columnas):
        matrizP[i].append(None)

for j in range (0,filas):
    for i in range(0,columnas):
        matrizP[j][i]=int(input(f"Digite un numero para la posicion [{[j+1]}{[i+1]}] : "))

print("Matriz original")
for fila in matrizP:
    for elemento in fila:
        print(f"{elemento}", end=" ")
    print()

posicion1=int(input("Digite la fila en la que quiere poner el entero: "))
posicion2=int(input("Digite la columna en la quiere poner el entero: "))
matrizP[posicion1-1][posicion2-1]= int(entero)

print("Matriz resultante")
for fila in matrizP:
    for elemento in fila:
        print(f"{elemento}", end=" ")
    print()