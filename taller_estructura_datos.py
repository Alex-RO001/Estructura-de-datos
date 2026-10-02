


# Compatibilidad para evitar advertencias del analizador sobre 'print'
if "print" not in globals():
    def print(*args, **kwargs):
        import builtins
        return builtins.print(*args, **kwargs)


print("\n=================================")
print("     EJERCICIO 1 - ESTUDIANTE")
print("=================================")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
programa = input("Ingrese su programa académico: ")
semestre = int(input("Ingrese su semestre: "))

print("\n=================================")
print("      INFORMACIÓN DEL ESTUDIANTE")
print("=================================")
print("Nombre:", nombre)
print("Edad:", edad)
print("Programa:", programa)
print("Semestre:", semestre)





print("\n=================================")
print("     EJERCICIO 2 - NOTA")
print("=================================")

nota = float(input("Ingrese la nota definitiva (0.0 a 5.0): "))

if nota < 0.0 or nota > 5.0:
    print("La nota no es válida.")
elif nota >= 3.0:
    print("APROBADO")
else:
    print("REPROBADO")



print("\n=================================")
print("     EJERCICIO 3 - NÚMEROS")
print("=================================")

print("\nNúmeros del 1 al 100:")
for numero in range(1, 101):
    print(numero, end=" ")

print("\n\nNúmeros pares:")
for numero in range(1, 101):
    if numero % 2 == 0:
        print(numero, end=" ")

print("\n\nNúmeros impares:")
for numero in range(1, 101):
    if numero % 2 != 0:
        print(numero, end=" ")

print("\n\nMúltiplos de 5:")
for numero in range(1, 101):
    if numero % 5 == 0:
        print(numero, end=" ")

suma = 0

for numero in range(1, 101):
    suma = suma + numero

print("\n\nSuma de todos los números del 1 al 100:", suma)



def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None
    return a / b




print("\n=================================")
print("     EJERCICIO 4 - CALCULADORA")
print("=================================")

while True:
    print("\n=========================")
    print("      CALCULADORA")
    print("=========================")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Seleccione: ")

    if opcion == "5":
        print("Saliendo de la calculadora...")
        break

    if opcion in ["1", "2", "3", "4"]:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = sumar(numero1, numero2)
            print("Resultado:", resultado)

        elif opcion == "2":
            resultado = restar(numero1, numero2)
            print("Resultado:", resultado)

        elif opcion == "3":
            resultado = multiplicar(numero1, numero2)
            print("Resultado:", resultado)

        elif opcion == "4":
            resultado = dividir(numero1, numero2)

            if resultado is None:
                print("No se puede dividir entre cero.")
            else:
                print("Resultado:", resultado)
    else:
        print("Opción no válida.")




print("\n=================================")
print("     EJERCICIO 5 - NOTAS")
print("=================================")

nota1 = 3.5
nota2 = 4.2
nota3 = 2.8
nota4 = 4.5
nota5 = 3.9

notas = [nota1, nota2, nota3, nota4, nota5]

# Calcular promedio sin utilizar sum()
total = 0

for nota in notas:
    total = total + nota

promedio = total / len(notas)

# Buscar la mayor y la menor sin utilizar max() ni min()
mayor = notas[0]
menor = notas[0]

for nota in notas:
    if nota > mayor:
        mayor = nota

    if nota < menor:
        menor = nota

# Contar aprobados
aprobados = 0

for nota in notas:
    if nota >= 3.0:
        aprobados = aprobados + 1

print("Promedio:", promedio)
print("Mayor nota:", mayor)
print("Menor nota:", menor)
print("Cantidad de aprobados:", aprobados)






print("\n=================================")
print("     EJERCICIO 6 - ESTUDIANTES")
print("=================================")

estudiantes = [
    "Carlos",
    "María",
    "Juan",
    "Ana",
    "Pedro",
    "Laura",
    "Andrés",
    "Sofía",
    "Daniel",
    "Valentina"
]

print("\nTodos los estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

print("\nPrimer estudiante:", estudiantes[0])
print("Último estudiante:", estudiantes[-1])
print("Cantidad de estudiantes:", len(estudiantes))

nuevo_estudiante = input("\nIngrese un estudiante para agregar: ")
estudiantes.append(nuevo_estudiante)

print("\nLista después de agregar:")
for estudiante in estudiantes:
    print(estudiante)

estudiante_eliminar = input("\nIngrese el estudiante que desea eliminar: ")

if estudiante_eliminar in estudiantes:
    estudiantes.remove(estudiante_eliminar)
    print("Estudiante eliminado.")
else:
    print("Ese estudiante no está en la lista.")

estudiante_buscar = input("\nIngrese el estudiante que desea buscar: ")

if estudiante_buscar in estudiantes:
    print("El estudiante fue encontrado.")
else:
    print("El estudiante no fue encontrado.")





print("\n=================================")
print("     EJERCICIO 7 - NOTAS")
print("=================================")

notas = [3.5, 4.2, 2.8, 4.5, 3.9, 2.5, 4.0, 4.7]

# Número de estudiantes
cantidad_estudiantes = len(notas)

# Promedio sin utilizar sum()
total = 0

for nota in notas:
    total = total + nota

promedio = total / cantidad_estudiantes

# Mayor y menor sin utilizar max() ni min()
nota_mayor = notas[0]
nota_menor = notas[0]

for nota in notas:
    if nota > nota_mayor:
        nota_mayor = nota

    if nota < nota_menor:
        nota_menor = nota

# Cantidad de aprobados y reprobados
aprobados = 0
reprobados = 0

for nota in notas:
    if nota >= 3.0:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

# Notas mayores que el promedio
notas_mayores_promedio = []

for nota in notas:
    if nota > promedio:
        notas_mayores_promedio.append(nota)

print("Número de estudiantes:", cantidad_estudiantes)
print("Promedio:", promedio)
print("Nota mayor:", nota_mayor)
print("Nota menor:", nota_menor)
print("Cantidad de aprobados:", aprobados)
print("Cantidad de reprobados:", reprobados)
print("Notas mayores que el promedio:", notas_mayores_promedio)




print("\n=================================")
print("     EJERCICIO 8 - BÚSQUEDA")
print("=================================")

productos = [
    "Teclado",
    "Mouse",
    "Monitor",
    "Impresora",
    "Memoria RAM",
    "Disco SSD"
]

producto_buscar = input("Ingrese el producto que desea buscar: ")

encontrado = False

for producto in productos:
    if producto.lower() == producto_buscar.lower():
        encontrado = True
        break

if encontrado:
    print("Producto encontrado.")
else:
    print("Producto no encontrado.")






print("\n=================================")
print("     EJERCICIO 9 - MATRIZ")
print("=================================")

notas = [
    [4.0, 3.5, 4.2],
    [3.0, 4.1, 3.7],
    [4.5, 3.8, 4.0],
    [2.8, 3.2, 3.5],
    [3.9, 4.5, 4.2]
]

materias = ["Programación", "Matemáticas", "Inglés"]

print("\nPromedio de cada estudiante:")

promedios_estudiantes = []

for fila in notas:
    total = 0

    for nota in fila:
        total = total + nota

    promedio_estudiante = total / len(fila)
    promedios_estudiantes.append(promedio_estudiante)

for i in range(len(promedios_estudiantes)):
    print("Estudiante", i + 1, ":", promedios_estudiantes[i])


print("\nPromedio de cada asignatura:")

for columna in range(3):
    total = 0

    for fila in range(len(notas)):
        total = total + notas[fila][columna]

    promedio_asignatura = total / len(notas)

    print(materias[columna], ":", promedio_asignatura)


nota_mayor = notas[0][0]
nota_menor = notas[0][0]

for fila in notas:
    for nota in fila:
        if nota > nota_mayor:
            nota_mayor = nota

        if nota < nota_menor:
            nota_menor = nota

print("\nNota mayor:", nota_mayor)
print("Nota menor:", nota_menor)



print("\n==========================================")
print("       EJERCICIO 10 - SISTEMA")
print("==========================================")

estudiantes_sistema = [
    ["Carlos", 20, 4.2],
    ["María", 19, 3.8],
    ["Juan", 21, 2.7]
]


def registrar_estudiante():
    print("\n--- Registrar estudiante ---")

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    nota = float(input("Nota: "))

    if nota < 0.0 or nota > 5.0:
        print("La nota debe estar entre 0.0 y 5.0.")
        return

    estudiante = [nombre, edad, nota]
    estudiantes_sistema.append(estudiante)

    print("Estudiante registrado correctamente.")


def mostrar_estudiantes():
    print("\n--- Lista de estudiantes ---")

    if len(estudiantes_sistema) == 0:
        print("No hay estudiantes registrados.")
    else:
        for estudiante in estudiantes_sistema:
            print(
                "Nombre:", estudiante[0],
                "| Edad:", estudiante[1],
                "| Nota:", estudiante[2]
            )


def buscar_estudiante():
    print("\n--- Buscar estudiante ---")

    nombre_buscar = input("Ingrese el nombre del estudiante: ")
    encontrado = False

    for estudiante in estudiantes_sistema:
        if estudiante[0].lower() == nombre_buscar.lower():
            print("Estudiante encontrado.")
            print("Nombre:", estudiante[0])
            print("Edad:", estudiante[1])
            print("Nota:", estudiante[2])
            encontrado = True
            break

    if not encontrado:
        print("Estudiante no encontrado.")


def mostrar_promedio():
    print("\n--- Promedio general ---")

    if len(estudiantes_sistema) == 0:
        print("No hay estudiantes registrados.")
        return

    total = 0

    for estudiante in estudiantes_sistema:
        total = total + estudiante[2]

    promedio = total / len(estudiantes_sistema)

    print("Promedio general:", promedio)


def mostrar_mayor_nota():
    print("\n--- Mayor nota ---")

    if len(estudiantes_sistema) == 0:
        print("No hay estudiantes registrados.")
        return

    mayor = estudiantes_sistema[0]

    for estudiante in estudiantes_sistema:
        if estudiante[2] > mayor[2]:
            mayor = estudiante

    print("Estudiante:", mayor[0])
    print("Nota:", mayor[2])


def mostrar_menor_nota():
    print("\n--- Menor nota ---")

    if len(estudiantes_sistema) == 0:
        print("No hay estudiantes registrados.")
        return

    menor = estudiantes_sistema[0]

    for estudiante in estudiantes_sistema:
        if estudiante[2] < menor[2]:
            menor = estudiante

    print("Estudiante:", menor[0])
    print("Nota:", menor[2])


def mostrar_aprobados():
    print("\n--- Estudiantes aprobados ---")

    hay_aprobados = False

    for estudiante in estudiantes_sistema:
        if estudiante[2] >= 3.0:
            print(
                "Nombre:", estudiante[0],
                "| Nota:", estudiante[2]
            )
            hay_aprobados = True

    if not hay_aprobados:
        print("No hay estudiantes aprobados.")


while True:
    print("\n========================================")
    print("          SISTEMA DE ESTUDIANTES")
    print("========================================")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Mostrar promedio")
    print("5. Mostrar mayor nota")
    print("6. Mostrar menor nota")
    print("7. Mostrar aprobados")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_estudiante()

    elif opcion == "2":
        mostrar_estudiantes()

    elif opcion == "3":
        buscar_estudiante()

    elif opcion == "4":
        mostrar_promedio()

    elif opcion == "5":
        mostrar_mayor_nota()

    elif opcion == "6":
        mostrar_menor_nota()

    elif opcion == "7":
        mostrar_aprobados()

    elif opcion == "8":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida.")


