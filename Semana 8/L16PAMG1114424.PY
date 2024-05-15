print("Semana No. 16: Ejercicio 1")


import random

numbers = [random.randint(1, 100) for _ in range(10)]


print("\nSeleccione una opción:")
print("a. Mostrar los números ingresados.")
print("b. Mostrar el promedio del arreglo.")
print("c. Mostrar la longitud del arreglo.")
print("d. Encontrar y mostrar:")
print("i. La suma de posiciones pares")
print("ii. La suma de posiciones impares")

option = input("Ingrese la opción deseada: ")


if option == "a":
    print(numbers)
elif option == "b":
    average = sum(numbers) / len(numbers)
    print(f"El promedio del arreglo es: {average:.2f}")
elif option == "c":
    print(f"La longitud del arreglo es: {len(numbers)}")
elif option == "d":
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    print(f"La suma de posiciones pares es: {even_sum}")
    print(f"La suma de posiciones impares es: {odd_sum}")
else:
    print("Opción inválida")



#Ejercicio 2
print("Semana No. 16: Ejercicio 2")


rows = int(input("Ingrese la cantidad de filas: "))
cols = int(input("Ingrese la cantidad de columnas: "))


import random

matrix = [[random.randint(0, 1000) for _ in range(cols)] for _ in range(rows)]


even_count = 0
odd_count = 0
max_num = matrix[0][0]
min_num = matrix[0][0]

for row in matrix:
    for num in row:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num


print("\nEstadísticas:")
print(f"Cantidad de números pares: {even_count}")
print(f"Cantidad de números impares: {odd_count}")
print(f"Número mayor: {max_num}")
print(f"Número menor: {min_num}")
