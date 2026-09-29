import psutil

def mostrar_servicio(data):
    print(f"Nombre: {data.get('name')}")
    print(f"PID: {data.get('pid') or 'Sin PID'}")
    print(f"Estado: {data.get('status')}")
    print(f"Tipo de inicio: {data.get('start_type')}")
    print("------------------------------------------")

def mostrar_todos():
    for servicio in psutil.win_service_iter():
        mostrar_servicio(servicio)


def mostrar_filtrados():
    filtro = input("Filtro (iniciado/parado y manual/automático): ").lower().split()

    if len(filtro) not in (1, 2):
        print("Escribe una o dos palabras.")
        return

    estados = {"iniciado": "running", "parado": "stopped"}
    inicios = {"manual": "manual", "automático": "automatic",
               "automatico": "automatic"}
    
    if filtro[0] not in estados:
        print("El estado debe ser 'iniciado' o 'parado'.")
        return

    if len(filtro) == 2 and filtro[1] not in inicios:
        print("El tipo de inicio debe ser 'manual' o 'automático'.")
        return
    
        encontrados = 0

    for servicio in psutil.win_service_iter():
        datos = servicio.as_dict()

        coincide_estado = datos.get("status") == estados[filtro[0]]
        coincide_inicio = (
            len(filtro) == 1
            or datos.get("start_type") == inicios[filtro[1]]
        )

        if coincide_estado and coincide_inicio:
            mostrar_servicio(datos)
            encontrados += 1

    print(f"Servicios encontrados: {encontrados}")


def mostrar_descripcion():
    nombre = input("Nombre del servicio: ").strip()
    servicio = psutil.win_service_get(nombre)
    print(f"Descripción: {servicio.description()}")
    
    
    
while True:
    print("\n1. Mostrar todos los servicios")
    print("2. Mostrar servicios filtrados")
    print("3. Mostrar descripción de un servicio")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_todos()
    elif opcion == "2":
        mostrar_filtrados()
    elif opcion == "3":
        mostrar_descripcion()
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")