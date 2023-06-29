import random

#Función para validar el dni
def validar_dni(dni):
    dni = dni.replace(".","").replace("-","")
    dv = dni[-1]
    cuerpo = dni[:-1]
    if not cuerpo.isdigit():
        return False
    suma = 0
    multiplicador = 2
    for i in range(len(cuerpo)-1,-1,-1):
        suma += int(cuerpo[i]) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    resto = suma % 11
    if resto == 0:
        dv_calculado = "0"
    elif resto == 1:
        dv_calculado = "K"
    else:
        dv_calculado = str(11 - resto)
    if dv_calculado.upper() == dv.upper():
        return True
    else:
        return False
    
# Mensaje de bienvenida
print("Bienvenido al sistema del Registro Nacional de Personas de la República de Argentina (RENAPER).")

#Menú de opciones
def mostrar_menu():
    print("Menú de opciones:")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Eliminar")
    print("5. Salir")

personas = []

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")
    # Verificamos que la opción sea válida
    if opcion not in ["1","2","3","4","5"]:
        print("Opción inválida, intente nuevamente.")
        continue
    #Menú de grabar
    dni_error = True
    nombre_error = True
    edad_error = True
    if opcion == "1":
        print("Opción 1: Grabar")
        while dni_error == True:
            dni = input("Ingrese el DNI: ")
            if not validar_dni(dni):
                print("dni inválido, intente nuevamente.")
            else:
                dni_error = False
                continue
        while nombre_error == True:
            nombre = input("Ingrese el nombre: ")
            if len(nombre) < 8:
                print("Nombre demasiado corto, intente nuevamente.")
            else:
                nombre_error = False
                continue
        while edad_error == True:
            edad = input("Ingrese la edad: ")
            try:
                edad = int(edad)
                if edad < 0:
                    print("Edad inválida, intente nuevamente.")
                else:
                    edad_error = False
                    continue
            except ValueError:
                print("Edad inválida, intente nuevamente.")
        pais = input("Ingrese el país de nacimiento: ")
        ciudad = input("Ingrese la ciudad de nacimiento: ")
        persona = {"dni": dni, "nombre": nombre, "edad": edad, "pais": pais, "ciudad": ciudad}
        personas.append(persona)
        print(f"Se ha grabado a {nombre} con éxito en la base de datos.")
    
    #Menú de búsqueda
    elif opcion == "2":
        print("Opción 2: Buscar")
        dni = input("Ingrese el DNI a buscar: ")
        if not validar_dni(dni):
            print("dni inválido, intente nuevamente.")
            continue
        encontrado = False
        for persona in personas:
            if persona["dni"] == dni:
                encontrado = True
                print(f"Se ha encontrado a {persona['nombre']}.")
                print(f"DNI: {persona['dni']}")
                print(f"Edad: {persona['edad']}")
                print(f"País de nacimiento: {persona['pais']}")
                print(f"Ciudad de nacimiento: {persona['ciudad']}")
                if persona["pais"].lower() == "argentina":
                    print(f"{persona['nombre']} pertenece al país de Argentina.")
                else:
                    print(f"{persona['nombre']} no pertenece al país de Argentina.")
                break
        if not encontrado:
            print("No se ha encontrado a ninguna persona con ese DNI.")
    
    # Menú de certificados
    elif opcion == "3":
        print("Opción 3: Imprimir certificados")
        dni = input("Ingrese el DNI de la persona: ")
        if not validar_dni(dni):
            print("DNI inválido, intente nuevamente.")
            continue
        encontrado = False
        for persona in personas:
            if persona["dni"] == dni:
                encontrado = True
                nacimiento = random.randint(1000, 9999)
                conyugal = random.randint(1000, 9999)
                argentina = random.randint(1000, 9999)
                # Lista con los datos mezclados aleatoriamente
                datos = [f"dni: {persona['dni']}", f"Nombre: {persona['nombre']}", f"País de nacimiento: {persona['pais']}", f"Ciudad de nacimiento: {persona['ciudad']}"]
                random.shuffle(datos)
                # Certificados con los datos en orden aleatorio
                print(f"Certificado de nacimiento: {nacimiento}")
                for dato in datos:
                    print(dato)
                print()
                random.shuffle(datos)
                print(f"Certificado de estado conyugal: {conyugal}")
                for dato in datos:
                    print(dato)
                print()
                random.shuffle(datos)
                print(f"Certificado de pertenencia al país de Argentina: {argentina}")
                for dato in datos:
                    print(dato)
                if persona["pais"].lower() == "argentina":
                    print(f"Pertenece al país de Argentina.")
                else:
                    print(f"No pertenece al país de Argentina.")
                
    # Menú de eliminación
    elif opcion == "4":
        print("Opción 4: Eliminar")
        dni = input("Ingrese el DNI a eliminar: ")
        if not validar_dni(dni):
            print("DNI inválido, intente nuevamente.")
            continue
        encontrado = False
        for i in range(len(personas)):
            if personas[i]["dni"] == dni:
                encontrado = True
                nombre = personas[i]["nombre"]
                del personas[i]
                print(f"Se ha eliminado a {nombre} de la base de datos con éxito.")
                break
        if not encontrado:
            print("No se ha encontrado a ninguna persona con ese DNI.")

    # Menú de salida
    elif opcion == "5":
        print("Opción 5: Salir")
        print("Gracias por usar el servicio de Autoatención de RENAPER.\nDesarrollado por Gabriel Balbontín \nVersión 1.0\nHasta pronto.")
        break

