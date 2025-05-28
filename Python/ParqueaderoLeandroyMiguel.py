fila = 8
columna = 8
mapa = [
    ["E", "-", "-", "-", "-", "-", "-", "-"],
    ["V", "V", "V", "V", "V", "V", "V", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "V", "V", "V", "V", "V", "V", "V"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["V", "V", "V", "V", "V", "V", "V", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["S", "V", "V", "V", "V", "V", "V", "V"],
]

vehiculos = {}
dinero = 0

def mostrar_mapa():
    for fila in mapa:
        print(" ", fila)

def espacios_disponibles():
    libres = 0
    for i in range(8):
        for j in range(8):
            if mapa[i][j] == "V":
                libres += 1

    print(f"Espacios disponibles: {libres}")
    print("Vista como dios del parqueadero:")
    for fila in mapa:
        print(" ", " ".join(fila))
    return libres

def estadisticas():
    carros = 0
    motos = 0
    for datos in vehiculos.values():
        if datos[3] == "carro":
            carros += 1
        elif datos[3] == "moto":
            motos += 1

    print("Estadísticas del sistema")
    print(f"Vehículos en parqueadero: {len(vehiculos)}")
    print(f"Carros: {carros}")
    print(f"Motos: {motos}")
    espacios_disponibles()
    print(f"Dinero recaudado: ${dinero}")

def buscar_espacio():
    for i in range(8):
        for j in range(8):
            if mapa[i][j] == "V":
                return i, j
    return None

def ingresar():
    placa = input("Placa del vehículo: ")
    tipo = input("¿Es carro o moto?: ")

    if tipo not in ["carro", "moto"]:
        print("Tipo no válido.")
        return

    lugar = buscar_espacio()
    if not lugar:
        print("No hay espacio disponible.")
        return

    hora = int(input("Hora de entrada (0-23): "))
    minutos = int(input("Minutos (0-59): "))
    entrada = hora * 60 + minutos

    i, j = lugar
    mapa[i][j] = "O" if tipo == "carro" else "M"
    vehiculos[placa] = [i, j, entrada, tipo]
    print(f"{tipo.capitalize()} con placa {placa} ingresado en ({i},{j})")  

    estadisticas()

def retirar():
    global dinero
    placa = input("Placa del vehículo a retirar: ")

    if placa not in vehiculos:
        print("Vehículo no encontrado.")
        return

    hora = int(input("Hora de salida (0-23): "))
    minutos = int(input("Minutos (0-59): "))
    salida = hora * 60 + minutos

    i, j, entrada, tipo = vehiculos[placa]
    tiempo = salida - entrada
    if tiempo <= 0:
        print("Error: la salida debe ser después de la entrada.")
        return

    tarifa = 100 if tipo == "carro" else 50
    total = tiempo * tarifa
    dinero += total

    mapa[i][j] = "V"
    del vehiculos[placa]

    print(f"Vehículo {placa} retirado.")
    print(f"Tiempo: {tiempo} minutos")
    print(f"Total a pagar: ${total}")

    estadisticas()

def menu():
    while True:
        print("Menú del Super Parqueadero Miguel y Leandro")
        print("1. Ingresar vehículo")
        print("2. Retirar vehículo")
        print("3. Ver mapa actual")
        print("4. Ver estadísticas")
        print("5. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            ingresar()
        elif opcion == "2":
            retirar()
        elif opcion == "3":
            espacios_disponibles()
        elif opcion == "4":
            estadisticas()
        elif opcion == "5":
            print("Gracias por usar nuestro sistema de parqueadero. Profe, pónganos 50 :)")
            break
        else:
            print("Opción no válida.")

menu()
