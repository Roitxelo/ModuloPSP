import json
from datetime import datetime
from pathlib import Path

import psutil


def obtener_informacion():
    particiones = []

    for particion in psutil.disk_partitions():
        try:
            uso = psutil.disk_usage(particion.mountpoint)
        except (PermissionError, OSError):
            continue

        particiones.append({
            "unidad": particion.device,
            "ruta": particion.mountpoint,
            "sistema_archivos": particion.fstype,
            "total_bytes": uso.total,
            "usado_bytes": uso.used,
            "libre_bytes": uso.free,
            "porcentaje_usado": uso.percent
        })

    disco = psutil.disk_io_counters()
    red = psutil.net_io_counters()
    memoria = psutil.virtual_memory()

    return {
        "plataforma": "Windows" if psutil.WINDOWS else "Linux",
        "cpu": {
            "numero": psutil.cpu_count(),
            "frecuencia_mhz": [
                frecuencia.current
                for frecuencia in psutil.cpu_freq(percpu=True)
            ],
            "uso_por_cpu_porcentaje": psutil.cpu_percent(interval=1, percpu=True)
        },
        "memoria": {
            "total_bytes": memoria.total,
            "disponible_bytes": memoria.available,
            "porcentaje_usado": memoria.percent
        },
        "discos": {
            "particiones": particiones,
            "operaciones_lectura": disco.read_count,
            "operaciones_escritura": disco.write_count,
            "bytes_leidos": disco.read_bytes,
            "bytes_escritos": disco.write_bytes
        },
        "red": {
            "bytes_enviados": red.bytes_sent,
            "bytes_recibidos": red.bytes_recv,
            "paquetes_enviados": red.packets_sent,
            "paquetes_recibidos": red.packets_recv
        }
    }


while True:
    print("\n1. Mostrar información del sistema")
    print("2. Guardar información del sistema")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        informacion = obtener_informacion()
        print(json.dumps(informacion, indent=2, ensure_ascii=False))

    elif opcion == "2":
        ruta = Path(input("Ruta de la carpeta donde guardar el JSON: ").strip())

        if not ruta.is_dir():
            print("La carpeta indicada no existe.")
            continue

        informacion = obtener_informacion()
        nombre = datetime.now().strftime("%Y%m%d%H%M%S") + "-system-info.json"
        archivo = ruta / nombre

        with open(archivo, "w", encoding="utf-8") as fichero:
            json.dump(informacion, fichero, indent=2, ensure_ascii=False)

        print(f"Información guardada en: {archivo}")

    elif opcion == "3":
        break

    else:
        print("Opción no válida.")