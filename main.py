# este maneja toda la logica principal de mi codigo 
import os
os.system("cls")
from functions import *

anio_actual = 2026
nombre = "Cristobal"
saludar()
print("*****************************")
obtener_nombre(nombre)
print("*****************************")
retorno_anio = obtener_anio(anio_actual)
print(f"El año actual es: {anio_actual}")
print("*****************************")

