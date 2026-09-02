"""
Algoritmo: inventario_biblioteca
Traduccion de PSeInt a Python, conservando la logica original.
"""

import os


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausa(mensaje="Presione ENTER para continuar."):
    input(mensaje)


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero entero valido.")


def main():
    # ------------------------------------------------------------
    # Datos iniciales (equivalentes a los arreglos del PSeInt)
    # ------------------------------------------------------------
    libros = [
        "Batman: Year One",
        "Resident Evil Archives",
        "El arte de crear",
        "El Principito",
        "El Arte de la Guerra",
        "Cien Años de Soledad",
        "Don Quijote",
        "1984",
        "Fahrenheit 451",
        "Dracula",
    ]
    stock = [2] * 10  # indice 0 = libro 1, ... indice 9 = libro 10

    # usuarios: lista de diccionarios {nombre, codigo, telefono}
    usuarios = [
        {"nombre": "Usuario 1/ Neithan Durant", "codigo": "1234", "telefono": "99999999"},
        {"nombre": "Usuario 2/ Jose Carranza", "codigo": "1010", "telefono": "88888888"},
    ]

    # prestamos: lista de diccionarios
    # {usuario, libro (id 1-10), dia, mes, anio,
    #  venc_dia, venc_mes, venc_anio, estado, cargo}
    prestamos = []

    salir_sistema = False

    # ------------------------------------------------------------
    # Bucle principal
    # ------------------------------------------------------------
    while not salir_sistema:

        acceso = False
        codigo_ingresado = ""

        # --------------------------------------------------------
        # Pantalla de acceso
        # --------------------------------------------------------
        while not acceso and not salir_sistema:

            limpiar_pantalla()
            print("=========================================")
            print("          BIBLIOTECA - ACCESO")
            print("=========================================")
            print("1. Tengo una cuenta")
            print("2. Crear una cuenta")
            print("3. Salir")
            print("-----------------------------------------")
            tiene_cuenta = input("Seleccione una opcion: ")

            if tiene_cuenta == "1":
                limpiar_pantalla()
                print("=========================================")
                print("        INGRESO A LA BIBLIOTECA")
                print("=========================================")

                usuario_encontrado = False

                while not usuario_encontrado and not acceso:

                    print("Ingrese su codigo de usuario.")
                    print("Escriba 0 para regresar al inicio.")
                    print("-----------------------------------------")
                    codigo_ingresado = input()

                    if codigo_ingresado == "0":
                        codigo_ingresado = ""
                        usuario_encontrado = True  # sale del bucle interno hacia el menu de acceso

                    else:
                        usuario_encontrado = any(
                            u["codigo"] == codigo_ingresado for u in usuarios
                        )

                        if usuario_encontrado:
                            acceso = True
                            print()
                            print("=========================================")
                            print("          ACCESO CORRECTO")
                            print("=========================================")
                            print("Bienvenido/a a la biblioteca.")
                            print("=========================================")
                            pausa()

                        else:
                            print()
                            print("=========================================")
                            print("             ALERTA")
                            print("=========================================")
                            print("El codigo no esta registrado.")
                            print("=========================================")
                            print()
                            print("1. Intentar nuevamente")
                            print("2. Crear una cuenta")
                            print("3. Regresar al inicio")
                            print("-----------------------------------------")
                            opcion_acceso = leer_entero("Seleccione una opcion: ")

                            if opcion_acceso == 1:
                                limpiar_pantalla()
                                print("=========================================")
                                print("        INTENTAR NUEVAMENTE")
                                print("=========================================")
                                print()
                                usuario_encontrado = False

                            elif opcion_acceso == 2:
                                limpiar_pantalla()
                                print("=========================================")
                                print("             CREAR CUENTA")
                                print("=========================================")
                                nombre_ingresado = input("Ingrese su nombre completo: ")
                                telefono_ingresado = input("Ingrese su numero de telefono: ")

                                tam = len(telefono_ingresado)

                                if tam >= 4:
                                    codigo_ingresado = telefono_ingresado[tam - 4:tam]
                                    usuarios.append({
                                        "nombre": nombre_ingresado,
                                        "codigo": codigo_ingresado,
                                        "telefono": telefono_ingresado,
                                    })

                                    usuario_encontrado = True
                                    acceso = True

                                    print()
                                    print("=========================================")
                                    print("          REGISTRO EXITOSO")
                                    print("=========================================")
                                    print("Nombre:", nombre_ingresado)
                                    print("Telefono:", telefono_ingresado)
                                    print("Codigo de usuario:", codigo_ingresado)
                                    print("=========================================")
                                    pausa()

                                else:
                                    print()
                                    print("El telefono debe tener al menos 4 digitos.")
                                    pausa()
                                    usuario_encontrado = False

                            elif opcion_acceso == 3:
                                usuario_encontrado = True
                                acceso = False

                            else:
                                print("Opcion no valida.")
                                pausa()
                                usuario_encontrado = False

            elif tiene_cuenta == "2":
                limpiar_pantalla()
                print("=========================================")
                print("             CREAR CUENTA")
                print("=========================================")
                nombre_ingresado = input("Ingrese su nombre completo: ")
                telefono_ingresado = input("Ingrese su numero de telefono: ")

                tam = len(telefono_ingresado)

                if tam >= 4:
                    codigo_ingresado = telefono_ingresado[tam - 4:tam]
                    usuarios.append({
                        "nombre": nombre_ingresado,
                        "codigo": codigo_ingresado,
                        "telefono": telefono_ingresado,
                    })

                    acceso = True

                    print()
                    print("=========================================")
                    print("          REGISTRO EXITOSO")
                    print("=========================================")
                    print("Nombre:", nombre_ingresado)
                    print("Telefono:", telefono_ingresado)
                    print("Codigo de usuario:", codigo_ingresado)
                    print("=========================================")
                    pausa()

                else:
                    print()
                    print("El telefono debe tener al menos 4 digitos.")
                    pausa()

            elif tiene_cuenta == "3":
                print()
                print("Gracias por utilizar la biblioteca.")
                salir_sistema = True

            else:
                print()
                print("Opcion no valida.")
                print("Use 1, 2 o 3.")
                pausa()

        # --------------------------------------------------------
        # Menu principal (una vez con acceso concedido)
        # --------------------------------------------------------
        if acceso and not salir_sistema:

            op = "1"

            while op != "0" and acceso:

                limpiar_pantalla()
                print("=========================================")
                print("          GESTION DE BIBLIOTECA")
                print("=========================================")
                print("Codigo de usuario:", codigo_ingresado)
                print("-----------------------------------------")
                print("1. Ver catalogo")
                print("2. Solicitar prestamo")
                print("3. Ver usuarios")
                print("4. Devolver libro")
                print("5. Ver alertas")
                print("0. Cerrar sesion")
                print("-----------------------------------------")
                op = input("Seleccione una opcion: ")

                # ---------------- 1. Ver catalogo ----------------
                if op == "1":
                    limpiar_pantalla()
                    print("=========================================")
                    print("          CATALOGO DE LIBROS")
                    print("=========================================")

                    for i in range(10):
                        if stock[i] > 0:
                            print(f"{i + 1}. {libros[i]} | Disponibles: {stock[i]}")
                        else:
                            print(f"{i + 1}. {libros[i]} | NO DISPONIBLE")

                    print("=========================================")
                    print("El numero indica cuantos ejemplares quedan.")
                    pausa("Presione ENTER para regresar.")

                # ---------------- 2. Solicitar prestamo ----------------
                elif op == "2":
                    limpiar_pantalla()
                    print("=========================================")
                    print("          SOLICITAR PRESTAMO")
                    print("=========================================")

                    for u in usuarios:
                        if u["codigo"] == codigo_ingresado:
                            print("Usuario:", u["nombre"])
                            print("Telefono:", u["telefono"])

                    print("Codigo:", codigo_ingresado)
                    print("-----------------------------------------")
                    cantidad_libros = leer_entero("Cuantos libros desea sacar? (1 a 5) ")

                    if 1 <= cantidad_libros <= 5:

                        dia_prestamo = leer_entero("Dia del prestamo: ")
                        mes_prestamo = leer_entero("Mes del prestamo: ")
                        anio_prestamo = leer_entero("Año del prestamo: ")

                        dia_devolucion = dia_prestamo + 7
                        mes_devolucion = mes_prestamo
                        anio_devolucion = anio_prestamo

                        if dia_devolucion > 30:
                            dia_devolucion -= 30
                            mes_devolucion += 1

                        if mes_devolucion > 12:
                            mes_devolucion = 1
                            anio_devolucion += 1

                        for j in range(1, cantidad_libros + 1):
                            print()
                            print(f"Libro {j} de {cantidad_libros}")
                            codigo_libro = leer_entero("Ingrese ID del libro (1-10): ")

                            if 1 <= codigo_libro <= 10:
                                idx = codigo_libro - 1
                                if stock[idx] > 0:
                                    prestamos.append({
                                        "usuario": codigo_ingresado,
                                        "libro": codigo_libro,
                                        "dia": dia_prestamo,
                                        "mes": mes_prestamo,
                                        "anio": anio_prestamo,
                                        "venc_dia": dia_devolucion,
                                        "venc_mes": mes_devolucion,
                                        "venc_anio": anio_devolucion,
                                        "estado": "PRESTADO",
                                        "cargo": 0,
                                    })

                                    stock[idx] -= 1

                                    print("Libro agregado correctamente.")
                                    print("Disponibles ahora:", stock[idx])

                                else:
                                    print("NO HAY EJEMPLARES DISPONIBLES.")

                            else:
                                print("ID de libro incorrecto.")

                        print()
                        print("=========================================")
                        print("           RECIBO DE PRESTAMO")
                        print("=========================================")
                        print("Usuario:", codigo_ingresado)
                        print(f"Fecha: {dia_prestamo}/{mes_prestamo}/{anio_prestamo}")
                        print(f"Devolucion: {dia_devolucion}/{mes_devolucion}/{anio_devolucion}")
                        print("-----------------------------------------")
                        print("LIBROS PRESTADOS:")

                        for p in prestamos:
                            if p["usuario"] == codigo_ingresado and p["estado"] == "PRESTADO":
                                print("-", libros[p["libro"] - 1])

                        print("-----------------------------------------")
                        print("Multa por atraso: L.100 por dia.")
                        print("=========================================")

                    else:
                        print("Cantidad no valida. Debe ser de 1 a 5.")

                    print()
                    pausa("Presione ENTER para regresar.")

                # ---------------- 3. Ver usuarios ----------------
                elif op == "3":
                    limpiar_pantalla()
                    print("=========================================")
                    print("        USUARIOS REGISTRADOS")
                    print("=========================================")

                    for idx_u, u in enumerate(usuarios, start=1):
                        print()
                        print(f"Usuario #{idx_u}")
                        print("Nombre:", u["nombre"])
                        print("Codigo:", u["codigo"])
                        print("Telefono:", u["telefono"])
                        print("-----------------------------------------")

                        encontrado = False

                        for p in prestamos:
                            if p["usuario"] == u["codigo"]:
                                encontrado = True
                                print("Libro:", libros[p["libro"] - 1])
                                print("Estado:", p["estado"])
                                print(f"Prestamo: {p['dia']}/{p['mes']}/{p['anio']}")
                                print(f"Vence: {p['venc_dia']}/{p['venc_mes']}/{p['venc_anio']}")
                                print("Multa: L.", p["cargo"])
                                print("-----------------------------------------")

                        if not encontrado:
                            print("Sin historial de prestamos.")

                    print()
                    pausa("Presione ENTER para regresar.")

                # ---------------- 4. Devolver libro ----------------
                elif op == "4":
                    limpiar_pantalla()
                    print("=========================================")
                    print("             DEVOLUCION")
                    print("=========================================")
                    codigo_libro = leer_entero("ID del libro que desea devolver: ")

                    dia_actual = leer_entero("Dia actual: ")
                    mes_actual = leer_entero("Mes actual: ")
                    anio_actual = leer_entero("Año actual: ")

                    dias_actuales = anio_actual * 360 + mes_actual * 30 + dia_actual
                    encontrado = False

                    for p in prestamos:
                        if (p["usuario"] == codigo_ingresado
                                and p["libro"] == codigo_libro
                                and p["estado"] == "PRESTADO"):

                            encontrado = True

                            dias_vencimiento = (p["venc_anio"] * 360
                                                 + p["venc_mes"] * 30
                                                 + p["venc_dia"])
                            dias_atraso = dias_actuales - dias_vencimiento

                            cargo = dias_atraso * 100 if dias_atraso > 0 else 0

                            p["cargo"] = cargo
                            p["estado"] = "DEVUELTO"
                            stock[codigo_libro - 1] += 1

                            print()
                            print("=========================================")
                            print("          DEVOLUCION COMPLETADA")
                            print("=========================================")
                            print("Usuario:", codigo_ingresado)
                            print("Libro:", libros[codigo_libro - 1])
                            print(f"Vencimiento: {p['venc_dia']}/{p['venc_mes']}/{p['venc_anio']}")
                            print(f"Devolucion: {dia_actual}/{mes_actual}/{anio_actual}")
                            print("Dias de atraso:", dias_atraso)
                            print("Cargo total: L.", cargo)
                            print("Disponibles ahora:", stock[codigo_libro - 1])
                            print("Estado: DEVUELTO")
                            print("=========================================")

                    if not encontrado:
                        print()
                        print("No se encontro un prestamo activo")
                        print("de este libro para este usuario.")

                    print()
                    pausa("Presione ENTER para regresar.")

                # ---------------- 5. Ver alertas ----------------
                elif op == "5":
                    limpiar_pantalla()
                    print("=========================================")
                    print("          ALERTAS DE PRESTAMOS")
                    print("=========================================")
                    print("Aqui aparecen los prestamos de TODOS")
                    print("los usuarios registrados.")
                    print("=========================================")

                    dia_actual = leer_entero("Dia actual: ")
                    mes_actual = leer_entero("Mes actual: ")
                    anio_actual = leer_entero("Año actual: ")

                    dias_actuales = anio_actual * 360 + mes_actual * 30 + dia_actual
                    encontrado = False

                    for idx_p, p in enumerate(prestamos, start=1):
                        if p["estado"] == "PRESTADO":

                            encontrado = True

                            dias_vencimiento = (p["venc_anio"] * 360
                                                 + p["venc_mes"] * 30
                                                 + p["venc_dia"])
                            dias_atraso = dias_actuales - dias_vencimiento

                            print()
                            print("-----------------------------------------")
                            print(f"PRESTAMO #{idx_p}")

                            for u in usuarios:
                                if u["codigo"] == p["usuario"]:
                                    print("Usuario:", u["nombre"])
                                    print("Codigo:", u["codigo"])
                                    print("Telefono:", u["telefono"])

                            print("Libro:", libros[p["libro"] - 1])
                            print(f"Fecha de prestamo: {p['dia']}/{p['mes']}/{p['anio']}")
                            print(f"Fecha de vencimiento: {p['venc_dia']}/{p['venc_mes']}/{p['venc_anio']}")

                            if dias_atraso > 0:
                                cargo = dias_atraso * 100
                                p["cargo"] = cargo
                                print("ESTADO: VENCIDO")
                                print("Dias de atraso:", dias_atraso)
                                print("Multa acumulada: L.", cargo)

                            elif dias_atraso == 0:
                                print("ESTADO: VENCE HOY")

                            elif dias_atraso == -1:
                                print("ESTADO: FALTA 1 DIA")

                            elif dias_atraso == -2:
                                print("ESTADO: FALTAN 2 DIAS")

                            else:
                                print("ESTADO: VIGENTE")
                                print("Dias restantes:", -dias_atraso)

                    if not encontrado:
                        print()
                        print("No existen prestamos activos.")

                    print()
                    print("=========================================")
                    pausa("Presione ENTER para regresar.")

                # ---------------- 0. Cerrar sesion ----------------
                elif op == "0":
                    limpiar_pantalla()
                    print("=========================================")
                    print("          CERRANDO SESION")
                    print("=========================================")
                    print("Los datos de la biblioteca se conservaran.")
                    print("El siguiente usuario vera el stock actualizado.")
                    print("=========================================")
                    pausa()

                    acceso = False

                else:
                    print()
                    print("=========================================")
                    print("          OPCION NO VALIDA")
                    print("=========================================")
                    print("Use solamente los numeros del menu.")
                    pausa()


if __name__ == "__main__":
    main()