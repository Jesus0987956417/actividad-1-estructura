import requests import re

url = "https://raw.githubusercontent.com/elastic/examples/refs/heads/master/Common%20Data%20Formats/apache_logs/apache_logs"

respuesta = requests.get(url) logs = respuesta.text

patron_ip = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}" ips = re.findall(patron_ip, logs)

patron_fecha_hora = r"[(\d{2}/[A-Za-z]+/\d{4}):(\d{2}:\d{2}:\d{2}) +\d{4}]" fechas_horas = re.findall(patron_fecha_hora, logs)

if ips and fechas_horas: for ip, (fecha, hora) in zip(ips, fechas_horas): print(f'IP: {ip}, Fecha: {fecha}, Hora: {hora}') else: print("No se encontraron direcciones IP, fechas o horas.")
