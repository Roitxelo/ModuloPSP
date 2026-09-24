import psutil
import json
from datetime import datetime



print(f"Hola mundo soy Linux? {psutil.LINUX}" )
print(f"Hola mundo soy Windows? {psutil.WINDOWS}" )

print(f"Número de CPUs: {psutil.cpu_count()}")
print(f"Frecuencia de CPUs: {psutil.cpu_freq()}")
print(f"Frecuencia de CPUs: {psutil.cpu_times_percent()}")

print(f"Memoria total: {psutil.virtual_memory().total}")
print(f"Memoria disponible: {psutil.virtual_memory().available}")
print(f"Memoria usada (%): {psutil.virtual_memory().percent}")

print(f"Listado de particiones: {psutil.disk_partitions()}")
print(f"Uso de disco para cada unidad o partición: {psutil.disk_usage}")
print(f"Número de operaciones de lectura: {psutil.disk_io_counters().read_count}")
print(f"Número de operaciones de escritura: {psutil.disk_io_counters().write_count}")
print(f"Número de bytes leídos: {psutil.disk_io_counters().read_bytes}")
print(f"Número de bytes escritos: {psutil.disk_io_counters().write_bytes}")

print(f"Bytes enviados: {psutil.net_io_counters().bytes_sent}")
print(f"Bytes recibidos: {psutil.net_io_counters().bytes_recv}")
print(f"Paquetes enviados: {psutil.net_io_counters().dropout}")
print(f"Paquetes recibidos: {psutil.net_io_counters().dropin}")


result = {
    "linux"
}

output_file = datetime.now().strftime("%Y%m%d%H%M%S") + "-system-info.json"

with open(output_file, 'w') as file:
    json.dump(result, file, indent=2)

