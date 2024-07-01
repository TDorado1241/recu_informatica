notas_finales = []
notas_promediadas = []
def cargar_notas():
    cantidad_alumnos = int(input("Ingrese la cantidad de alumnos"))
    for nota1, nota2 in range(cantidad_alumnos):
        nota1 = int(input("ingresar la primera nota: "))
        notas_finales.append(nota1)
        nota2= int(input("ingresar la segunda nota: "))
        notas_finales.append(nota2)
    print()

def mostrar_notas():
    print(len(notas_finales))

def agregar_nota():
    nuevo_alumno = int(input("Ingresar las dos notas del nuevo alumno: "))
    if nuevo_alumno < 10 and nuevo_alumno > 0:
        notas_finales.append(nuevo_alumno)

def visualizar_promedio():
    promedio_total = sum(notas_promediadas)/len(notas_promediadas)
    print(promedio_total)

def ver_menor_nota():
    minima_nota = min(notas_finales)
    print(minima_nota)

def ver_cantidad_notas_mayores_o_igual_7():
    if notas_finales() <= 7:
        print()

while True:
    print("\n*** MENU DE OPCIONES ***")
    print("1. Cargar Notas de Alumnos.")
    print("2. Mostrar Notas de Alumnos.")
    print("3. Agregar Notas de un Alumno.")
    print("4. Visualizar el Promedio.")
    print("5. Ver la Menor Nota.")
    print("6. Ver Cantidad de Notas Mayor o igual a 7.")
    print("7. Eliminar al Primer Alumno Cargado.")
    print("8. Sumar un punto a los alumnos con nota 6.")
    print("0. Salir.")

    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        cargar_notas(notas_finales)
    elif opcion == 2:
        mostrar_notas(notas_finales)
    elif opcion == 3:
        agregar_nota(notas_finales)
    elif opcion == 4:
        visualizar_promedio(notas_finales)
    elif opcion == 5:
        ver_menor_nota(notas_finales)
    elif opcion == 6:
        ver_cantidad_notas_mayores_o_igual_7(notas_finales)
    elif opcion == 7:
        eliminar_primer_alumno(notas_finales)
    elif opcion == 8:
        sumar_punto_a_notas_seis(notas_finales)
    elif opcion == 0:
        print("Fin del Programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

