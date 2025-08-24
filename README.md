# REPOSITORIO DE STEVEN FERNANDO ARIAS GUAIGUA
El presente repositorio tiene como objetivo almacenar y exponer todos los trabajos presentados por el estudiante Steven Fernando Arias Guaigua, cursante de la carrera Ing. en Sistemas de la Informacion; asignatura de Logica de Programacion

## PRESENTACION DEL PROGRAMA
El trabajo que se presenta para la finalizacion de curso es un juego sumamente popular llamado: Piedra, Papel o Tijeras
Este juego sumamente simple en la vida real representa un pequeño pero significativo reto para los jovenes programadores
Puesto que promueve el pensamiento critico y la formulacion de un codigo que permita a la maquina realizar una eleccion
Al azar y mediante la comparativa, determinar el ganador e incluso si la opcion elegida no es valida

### ORIGEN DEL JUEGO
El juego piedra, papel o tijeras tiene su origen en China, donde se practicaba hace más de 2000 años bajo el nombre shoushiling. Posteriormente llegó a Japón, donde evolucionó como jan-ken 
con las mismas tres opciones modernas. A partir del siglo XX se difundió a Europa y América, convirtiéndose en un juego universal para resolver decisiones de manera rápida y justa.

#### IMPORTANCIA DEL JUEGO PARA APRENDICES DE PROGRAMACION BASICA
**Introducción a la lógica condicional**
Permite practicar estructuras como if, elif y else para determinar el ganador según las reglas.
**Manejo de entradas y salidas**
Ayuda a trabajar con funciones como input() y print() para interactuar con el usuario.
**Uso de bucles y control de flujo**
Se pueden usar while o for para repetir partidas, manejar errores y validar entradas.
**Pensamiento algorítmico**
Requiere estructurar reglas y condiciones de manera ordenada, fomentando la lógica computacional.
# Principios Básicos de la Programación y su Relación con la Lógica

La programación es el proceso de crear instrucciones que una computadora puede ejecutar para realizar tareas. Se fundamenta en principios que permiten organizar y estructurar estas instrucciones de manera lógica y eficiente.

---

## 1. Principios Básicos de la Programación

### 1.1 Secuencia
Las instrucciones se ejecutan en orden, de arriba hacia abajo.

```python
print("Primero")
print("Después")
```

### 1.2 Selección (Condicionales)
Permite tomar decisiones dentro de un programa según condiciones lógicas.

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### 1.3 Iteración (Bucles)
Permite repetir bloques de código mientras se cumpla una condición.

```python
for i in range(3):
    print("Repetición número", i)
```

### 1.4 Modularidad
Se basa en dividir un programa en partes más pequeñas y manejables (funciones).

```python
def saludo(nombre):
    print(f"Hola, {nombre}")

saludo("Ana")
```

---

#### 2. Lógica Básica de Programación

La lógica en programación consiste en aplicar **razonamiento ordenado** para resolver problemas. Incluye:

- **Operadores Lógicos**: `and` (y), `or` (o), `not` (no).  
- **Estructuras de Decisión**: para ejecutar acciones según condiciones.  
- **Algoritmos**: conjunto de pasos definidos para resolver un problema.

Ejemplo:

```python
llueve = True
paraguas = False

if llueve and not paraguas:
    print("Te vas a mojar")
else:
    print("Estás protegido")
```

---

##### 3. Comandos Básicos de Programación en Python

**3.1 Entrada y Salida**
```python
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)
```

**3.2 Variables y Tipos de Datos**
```python
edad = 25            # Entero
altura = 1.75        # Decimal (float)
nombre = "Carlos"    # Cadena de texto
activo = True        # Booleano
```

**3.3 Operadores**
- Aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparación: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Lógicos: `and`, `or`, `not`

**3.4 Condicionales**
```python
if edad >= 18:
    print("Acceso permitido")
else:
    print("Acceso denegado")
**3.5 Bucles**
# Bucle for
for i in range(5):
    print(i)

# Bucle while
contador = 0
while contador < 5:
    print(contador)
    contador += 1


## 4. Relación entre los Principios y la Lógica

- Secuencia, selección e iteración** son aplicados mediante estructuras de control.
- La **lógica** permite plantear condiciones y resolver problemas de manera correcta.
- Python, al ser un lenguaje sencillo, facilita entender estos principios y su aplicación práctica.
