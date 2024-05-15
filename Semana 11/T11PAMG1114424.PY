print("semana No. 11: Ejercicio 1")

N=0
while N<=0: 
    N=int(input("ingrese un número mayor que 0:"))
    if N<=0:
        print("el número ingresado debe ser mayor:")
        print()
A=0
B=1
C=0 
I=2
resultado=""
resultado=str(A)
if N>1:
    resultado+=("," +str(B))
    while I<N:
        C=A+B
        resultado+=(","+str(C))
        A=B
        B=C
        I=I+1 
    print(resultado)
else:
    print(resultado)


#Actividad 2

x = int(input("Ingrese un numero mayor a 0: "))
b = int(input("Ingrese un numero mayor a 0: "))
n = int(input("Ingrese un numero mayor a 0: "))

def calculo1(n):
    a = int(0)
    c = 0
    for i in range(n):
        a += 1
        c1 = 1/a
        c = c + c1
    print(c)
    
def calculo2(n):
    a = int(0)
    c = 0
    for i in range(n):
        a+=1
        c1 = 1/(2**a)
        c = c + c1
    print(c)

def calculo3(x,b,n):
    a = int(0)
    c = 1
    k = 1 
    
    for i in range(n):
        a +=1
        c1 = (x*a)(b**(a-k))
        k += 1
        c = c + c1
    print(c)
        
        


if n <= 0:
    print("Ingrese un numero valido, tiene que ser mayor a 0")
else:
    calculo1(n)
    calculo2(n)
    calculo3 (x,b,n)