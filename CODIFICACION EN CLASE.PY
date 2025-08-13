"""nombre = input ("Ingrese nombre");
apellido = input ("Ingrese apellido");
resultado = f"{nombre}{apellido}"
print (resultado)"""


"""nombre = input ("Ingrese nombre")
apellido = input ("Ingrese apellido")
nombre_completo = nombre + " " + apellido
print(nombre_completo)"""

"""x=True
y=False
print(x,y)"""

"""nota1 = float(input("Ingrese la primera calificacion"))
nota2 = float(input("Ingrese segunda nota"))
nota3 = float(input("Ingrese tercera nota"))
promedio = (nota1 + nota2 + nota3) / 3
print(promedio)"""


"""base = float(input("Ingrese la medida de la base (Puede tener decimales)"))
altura = float(input("Ingrese la medida de la altura (Puede tener decimales)"))
area_rectangulo = (base * altura)
print ("El area del rectangulo es:", area_rectangulo)"""


"""try:
    nombre = input ("Ingrese nombre")
    edad = int(input("Ingrese edad"))
    print("Hola, mi nombre es", nombre, "y mi edad es", edad)
except ValueError:
    print("Error, la edad debe ser escrita en numeros")"""



"""a = 2
b = 2
if (a == b):
    #print ('a = b')
    print ("son iguales")
else:
    print("son diferentes")"""


"""a=3
b=1
c=2

if(a==b):
    if b==c:
        print("Las 3 variables son identicas")
    else:
        print("a=b pero b y c son diferentes")
else:
    print("a y b son diferentes")"""


"""nombre=input("Ingrese su nombre ")
edad=int(input("Ingrese su edad "))
if edad < 18:
    print("Estimado", nombre,"su acceso ah sido negado puesto que usted es menor de edad")
else:
    print("Bienvenido", nombre, "su acceso ha sido aprobado")"""



"""#nombre de usuario es admin y la contraseña es 1234, sino contraseña incorrecta
nombre=input("Ingrese nombre de usuario: ")
if nombre==("admin"):
    contraseña=input("Ingrese la contraseña: ")
    if contraseña==("1234"):
        print("Bienvenido", nombre,"su acceso ha sido aprobado")
    else:
        print("Estimado", nombre,"por favor reinicie el programa e intente de nuevo con su contraseña")
else:
    print("Usuario no reconocido dentro de la base de datos")"""


"""a=input("Ingrese 1er numero: ")
b=input("ingrese 2do numero: ")
c=input("ingrese 3er numero: ")

if (a==b) and (b==c):
    print("Todos los numeros son iguales")
elif (a==b):
    print("Unicamente a y b son iguales, ergo, c es diferente")
else:
    print("Ninguno de los numeros ingresados es similar")"""




"""a=int(input("Ingrese numero cualquiera"))5
if a>5:
    print("Si cumple")
elif a<5:
    print ("no cumple")
elif a==5:
    print("Ingresar numero diferente")
else:
    print("Debe ingresar un numero, no una letra")"""


#Ingresar una nota por teclado (input) (entero, flotante o string) si es mayor a 18 es excelente, si es 14, es aprobado, si es mayor o igual a 10 necesita mejorar, sino directamente reprobado

"""nota=int(input("Ingrese la nota que haya obtenido en su examen: "))
if nota>=18:
    print("Ud ha aprobado con una calificacion excelente")
elif (nota<=17) and(nota>=14):
    print("Aprobado dentro de parametros estandar")
elif (nota<=13) and (nota>=10):
    print("Necesita mejorar su rendimiento")
elif nota<=9:
    print("No aprobado, repite materia")"""



"""i=0
suma=0
while i < 5:
   numero=float(input("Ingrese numero entero: "))
   suma+=numero
   i += 1
print("La sumatoria total es: ", suma)"""


i=0
numero=int(input("Ingrese un numero positivo: "))
while numero <= 0:
    print("No es un numero positivo")
    numero=int(input("Ingrese un numero positivo: "))

for i in range (0, numero+1):
    print(i)
