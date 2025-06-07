"""
Se solicita implementar una aplicación en Python para gestionar las notas de los
estudiantes de un curso, el programa deberá:
• Registrar estudiantes:
o Código del alumno, que tiene la forma Annnn (5 caracteres), donde nnnn son
dígitos, por ejemplo A0001
o Nombre
o apellido paterno
o apellido materno
o edad
o Nota trabajo
o Nota examen
o Participación
o Nota final, cuyo valor se calcula como el promedio aritmético de tres notas anteriores
• Esta información debe guardarse en un diccionario donde la clave sea el código delalumno
• Ante el error que pueda cometer un profesor, el programa deberá permitir buscar los
datos de un alumno (por su código) y permitirá actualizar sus tres notas (con ello se
actualizará también su promedio)
• Buscar un alumno y mostrar sus datos
• Listar los alumnos en orden descendente por el promedio
• Se debe crear un menú que maneje las distinta opciones definidas anteriormente
Se deberá emplear listas y diccionarios.
a) Registrar alumnos en el diccionario y calcular la nota final con los datos debidamente
validados 
b) Modificar notas 
c) Buscar alumno y mostrar sus datos
d) Listar los alumnos en orden descendente por el promedio 
e) Generar el Menú 
    
"""

def menu():
    print("1. Registrar estudiante ")
    print("2. Buscar y actualizar estudiante ")
    print("3. buscar estudiante ")
    print("4. Listar todos los esudiantes ")
    print("5. Salir ")
    opc=-1
    while opc<1 or opc>5:
        opc=int(input("Ingrese una opcion : "))
    return opc

def  registrar_alumno(dicc_alum):
    codigo=input("Ingrese su codigo a registarar : ")
    if len(codigo)==5:
        nombre=input("Ingrese su nombre : ")
        pat=input("ingrese su appellido paterno : ")
        mat=input("ingrese su apellido materno : ")
        edad=int(input("ingrese su edad : "))
        nota_trabajo=float(input("ingrese su nota de trabajo :"))
        nota_examen=float(input("ingrese su nota de examen :"))
        paticipacion=float(input("ingrese su nota de participacion :"))
        nota_final=(nota_trabajo+nota_examen+paticipacion)/3
        dicc_alum[codigo]=[nombre,pat,mat,edad,nota_trabajo,nota_examen,paticipacion]
        print("alumno registrad corectamente :) ")
    else:
        print("el codio debe tener solo 5 caracteres")

def modificar_notas(dic_alum):
    codigo=input("ingrese su codigo a modificar")
    if codigo in dic_alum:  #verifica si codigo existe
        nnota_trabajo=float(input("ingrese su nota de trabajo :"))
        nnota_examen=float(input("ingrese su nota de examen :"))
        npaticipacion=float(input("ingrese su nota de participacion :"))
        nota_final=(nnota_trabajo+nnota_examen+npaticipacion)/3
        dicc_alum[codigo][4]=nnota_trabajo
        dicc_alum[codigo][5]=nnota_examen
        dicc_alum[codigo][6]=npaticipacion
        dicc_alum[codigo][7]=nota_final
        print("Alumno modifica correctamente :) ")
        print(dicc_alum)
    else:
        print("no existe ese codigo ")

def buscar_alum(dicc_alum):
    codigo=input("ingrese su codigo a buscar")
    if codigo in dicc_alum:
        print(f"{dicc_alum[codigo]}")
    else:
        print("codigo no registrado ")


def listar_todos(dicc_alum):
    for clave,valor in dicc_alum.items():
        print(f"{clave} {valor}")


#Programa principal
dicc_alum=dict()
opc=1
while opc!=5:
    opc=menu()
    match opc:
        case 1:
            registrar_alumno(dicc_alum)
        case 2:
            modificar_notas(dicc_alum)


        case 3:
            buscar_alum(dicc_alum)
        case 4:
            listar_todos(dicc_alum)
        case 5:
            print("Gracias por usar el programa :) ")
