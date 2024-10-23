import zipfile
import os

def descomprimir_zip(ruta_zip, ruta_destino):
    # Verifica si el archivo ZIP existe
    if not os.path.exists(ruta_zip):
        print(f"El archivo {ruta_zip} no existe.")
        return

    # Crea la carpeta destino si no existe
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)

    # Descomprime el archivo ZIP
    with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
        zip_ref.extractall(ruta_destino)
        print(f"Archivo descomprimido en: {ruta_destino}")

# Ejemplo de uso
ruta_zip = 'Skyblock-1.20-Map.zip'  # Ruta del archivo ZIP
ruta_destino = 'servidor_minecraft'  # Carpeta donde se descomprimirá el contenido

descomprimir_zip(ruta_zip, ruta_destino)
