from turtle import *
import random

nombre=0
edad=0
color_favorito=color

print()
print("BIENVENIDO A CUENTOS DE UNA AVENTURA INESPERADA\nIngresa la siguiente información:\n")
nombre=str(input("Ingresa tu Nombre: "))
edad=int(input("Ingresa tu edad: "))
Color=int(input("Ingresa tu color favorito entre estas opciones numericas de los colores:\n\t(1. brown, 2. blue, 3. green, 4. yellow, 5. orange, )\n"))
# En este apartado se define un if para el color del triangulo en la historia, dependiendo del colorseleccionado, en la historia cambia el color y en el dibujo cambia la piramide de color.
if Color==1:
      colordibujar_triangul="brown"
elif Color==2:
      colordibujar_triangul="blue"
elif Color==3:
      colordibujar_triangul="green"
elif Color==4:
      colordibujar_triangul="yellow"
elif Color==5:
      colordibujar_triangul="orange"
# Se define cada objeto y dibujo por medio de turtle para agregarlas luego en las escenas.

def dibujar_burbujas():
    pendown()
    num_burbujas = 20
    for n in range(num_burbujas):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        radio = random.randint(5, 20)
        penup()
        goto(x, y)
        pendown()
        color("light blue")
        begin_fill()
        circle(radio)
        end_fill()
    
    penup()


    color("brown")


def sun():
    pendown()
    color("yellow")
    penup()
    goto(-350, 250)
    begin_fill()
    circle(100)
    end_fill()
    penup()


def grass():
    pendown()
    color("green")
    penup()
    goto(-400, -200)
    begin_fill()
    pendown()
    goto(600, -200)
    goto(600, -300)
    goto(-400, -300)
    goto(-400, -200)
    end_fill()
    penup()


def dibujar_caballo():
    pendown()
    i = 2
    x = 100
    y = -100
    hideturtle()
    fillcolor("brown")
    begin_fill()
    width(5)
    speed(50)
    penup()
    setpos(x, y)
    pendown()
    forward(30 / i)
    left(90)
    forward(50 / i)
    right(90)
    forward(50 / i)
    right(90)
    forward(50 / i)
    left(90)
    forward(30 / i)
    left(90)
    forward(100 / i)
    left(90)
    forward(80 / i)
    right(90)
    forward(60 / i)
    left(90)
    forward(50 / i)
    left(90)
    forward(20 / i)
    right(90)
    forward(20 / i)
    left(90)
    forward(40 / i)
    left(90)
    forward(40 / i)
    right(90)
    forward(100 / i)
    end_fill()
    left(90)
    forward(30 / i)
    left(90)
    penup()
    forward(120 / i)
    pendown()
    fillcolor("beige")
    begin_fill()
    right(90)
    forward(20 / i)
    right(90)
    forward(20 / i)
    left(90)
    forward(30 / i)
    right(90)
    forward(40 / i)
    right(90)
    forward(50 / i)
    right(90)
    forward(80 / i)
    end_fill()
    penup()


def dibujar_triangulo():
    pendown()
    fillcolor((colordibujar_triangul))
    penup()
    goto(-100, -100)  
    pendown()
    begin_fill()
    for _ in range(3):
        forward(200)
        left(120)
    end_fill()
    penup()


def caballo():
    pendown()
    i = 3
    x = -200
    y = -200
    hideturtle()
    fillcolor("brown")
    begin_fill()
    width(5)
    speed(50)
    penup()
    setpos(x, y)
    pendown()
    forward(30 / i)
    left(90)
    forward(50 / i)
    right(90)
    forward(50 / i)
    right(90)
    forward(50 / i)
    left(90)
    forward(30 / i)
    left(90)
    forward(100 / i)
    left(90)
    forward(80 / i)
    right(90)
    forward(60 / i)
    left(90)
    forward(50 / i)
    left(90)
    forward(20 / i)
    right(90)
    forward(20 / i)
    left(90)
    forward(40 / i)
    left(90)
    forward(40 / i)
    right(90)
    forward(100 / i)
    end_fill()
    left(90)
    forward(30 / i)
    left(90)
    penup()
    forward(120 / i)
    pendown()
    fillcolor("beige")
    begin_fill()
    right(90)
    forward(20 / i)
    right(90)
    forward(20 / i)
    left(90)
    forward(30 / i)
    right(90)
    forward(40 / i)
    right(90)
    forward(50 / i)
    right(90)
    forward(80 / i)
    end_fill()
    penup()


def dibujar_destellos():
    num_destellos = 100
    for _ in range(num_destellos):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        penup()
        goto(x, y)
        pendown()
        dot(random.randint(1, 5), "white")
    penup()


def dibujar_dunas():
    color("sandy brown")
    penup()
    goto(-400, -200)
    pendown()
    begin_fill()
    goto(400, -200)
    goto(400, -300)
    goto(-400, -300)
    goto(-400, -200)
    end_fill()
    hideturtle()

def dibujar_sol():
    color("yellow")
    penup()
    goto(-300, 200)
    begin_fill()
    circle(50)
    end_fill()
    hideturtle()

# Se definen las escenas y se les agrega los objetos realizados por turtle.turtle
def escena_1():
    reset()
    speed(0)
    hideturtle()
    setup(800, 600)

    bgcolor("deep sky blue")
    sun()
    grass()
    dibujar_caballo()
    dibujar_triangulo()
    print(f"Una vez, en un mundo mágico, vivía un niño llamado, {nombre}. {nombre} tenía {edad} años y su color favorito era {colordibujar_triangul} vivía en un mundo lleno de colores. Un día, mientras paseaba por el bosque cercano a su casa se encontro con su compañero de vida el camello Bartomeu, quien siempre lo acompañaba a todos lados,")


def escena_2():
    reset()
    speed(0)
    hideturtle()
    setup(800, 600)
    bgcolor("deep sky blue")  
    dibujar_burbujas()
    dibujar_caballo()
    print(f"Luego de dar una vuelta se econtraron con un triangulo triangulo flotante, el triangulo comenzo a sacudir y a sacar destellos de color verde, el triangulo lanzo rayos de color verde a Bartomeu y a {nombre} y se los llevo a lugares extraños pero increibles")


def escena_3():
    reset()
    speed(0)
    hideturtle()
    setup(800, 600) 
    bgcolor("black")  
    dibujar_destellos()
    dibujar_caballo()
    print(f"Primero visitaron el espacio, un lugar increible pero muy frio, lograban respirar al estar atrapados por los rayos verdes, Bartomeu temia las alturas, por lo que comenzo sentirse mal, luego de unas fasinantes vistas para {nombre} pasaron unos minutos y se esfumaron de nuevo, no sabian lo que les esperaba...")


def escena_4():
    reset()
    speed(0)
    hideturtle()
    setup(800, 600)
    bgcolor("deep sky blue")
    dibujar_sol()
    dibujar_dunas()
    caballo()
    print(f"Al despertar, no sabian donde se ecnontraban, comenzaron a ver burbujas y todo era muy azul, al observar bien y escuchar ruidos exraños, se dieron cuenta que estaban en el oceano, {nombre} entro en panico, ya que no sabia nadar y Bartomeu estaba flotando feliz mente en el agua, seguian protejidos por los rayos verdes y no se ahogaban, pero si escuchaban y sentian todo el oceano, jugaron por mucho tiempo, pero los rayos comenzaban a desaparecer, y sabian que algo podia pasar, luego de 4 horas de juego en el agua los rayos se fueron y ellos calleron en un sueño profundo...")


def escena_5():
    reset()
    speed(0)
    hideturtle()
    setup(800, 600)
    bgcolor("deep sky blue")
    sun()

    grass()
    dibujar_caballo()
    print(f"Luego de todo lo sucedido despertaron en el jardin de casa de {nombre}, Bartomeu estaba muy cansado por lo que se quedo en el jardin, no podian creer lo que les ocurrió, pero{nombre} y su querido amigo el camello Bartomeu le contaron a su madre la gran AVENTURA INESPERADA. FIN")

# Se agrega un menu de dibujo, para que el usuario pueda seleccionar un panel en especifico o pasar de secuancia por medio del pánel 
dibujar_menu = True
while dibujar_menu:
    Menudedibujos = int(input(("Ingresa el número de menú que deseas:\n1. Ver el cuento 'UNA AVENTURA INESPERADA'\n2. Ver un panel de dibujo\n3. Salir\n")))

    if Menudedibujos == 1:

        siguiente = 0
        while siguiente != 6:
            siguiente = int(input("Ingrese el número del panel siguiente (6 para salir): "))

            if siguiente == 1:
                escena_1()

            elif siguiente == 2:
                escena_2()

            elif siguiente == 3:
                escena_3()

            elif siguiente == 4:
                escena_4()

            elif siguiente == 5:
                escena_5()
            
            elif siguiente == 6:
                break

    elif Menudedibujos == 3:
        dibujar_menu = False

#si tu menu dice ver la secuencia 1:
#if menu==1:
#   siguiente=int(input("Ingrese el numero del panel siguiente"))
#        if siguiente==1:
#               escena_1()
#        elif siguiente==2:
#        exitonclick()