
print("Semana No. 12: Ejercicio 1")

print("Seleccione una opción:")
print("a. Área de triángulo")
print("b. Área de cuadrado")
print("c. Área de rectángulo")
print("d. Área de círculo")

option = input("Ingrese la opción deseada: ")

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_square_area(side):
    return side ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return 3.14 * (radius ** 2)

if option == "a":
    base = float(input("Ingrese la base del triángulo: "))
    height = float(input("Ingrese la altura del triángulo: "))
    area = calculate_triangle_area(base, height)
    print(f"El área del triángulo es: {area:.2f}")
elif option == "b":
    side = float(input("Ingrese el lado del cuadrado: "))
    area = calculate_square_area(side)
    print(f"El área del cuadrado es: {area:.2f}")
elif option == "c":
    length = float(input("Ingrese la longitud del rectángulo: "))
    width = float(input("Ingrese la anchura del rectángulo: "))
    area = calculate_rectangle_area(length, width)
    print(f"El área del rectángulo es: {area:.2f}")
elif option == "d":
    radius = float(input("Ingrese el radio del círculo: "))
    area = calculate_circle_area(radius)
    print(f"El área del círculo es: {area:.2f}")
else:
    print("Opción inválida")

# 1. texto de  "Semana No. 12: Ejercicio 2"
print("Semana No. 12: Ejercicio 2")

# 2. variables 
x = 0
y = 0

# 3. menú para el usuario 
while True:
    print("\nSeleccione una opción:")
    print("a. Sube")
    print("b. Baja")
    print("c. Izquierda")
    print("d. Derecha")
    print("e. Salir")

    option = input("Ingrese la opción deseada: ")

    if option == "a":
        mover_hacia_arriba() 
    elif option == "b":
        mover_hacia_abajo()
    elif option == "c":
        mover_hacia_izquierda()
    elif option == "d":
        mover_hacia_derecha()
    elif option == "e":
        break
    else:
        print("Opción inválida")

# 4. Def. funciones
def mover_hacia_arriba():
    global y
    y += 1
    print(f"Coordenadas actuales: {x}, {y}")

def mover_hacia_abajo():
    global y
    y -= 1
    print(f"Coordenadas actuales: {x}, {y}")

def mover_hacia_derecha():
    global x
    x += 1
    print(f"Coordenadas actuales: {x}, {y}")

def mover_hacia_izquierda():
    global x
    x -= 1
    print(f"Coordenadas actuales: {x}, {y}")
print(f"Coordenadas finales del personaje: {x}, {y}")