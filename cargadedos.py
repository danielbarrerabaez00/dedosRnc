import os
import shutil

# Ruta al directorio donde están las imágenes
src_directory = 'dedos'

# Ruta base para las nuevas carpetas
base_target_directory = 'dedos_ordenados'

# Crear el directorio base si no existe
if not os.path.exists(base_target_directory):
    os.makedirs(base_target_directory)

# Recorrer todos los archivos en el directorio de imágenes
for filename in os.listdir(src_directory):
    if filename.endswith(('0R', '1R', '2R', '3R', '4R', '5R', '0L', '1L', '2L', '3L', '4L', '5L')):
        # Extraer el código al final del nombre del archivo (últimos dos caracteres)
        code = filename[-2:]

        # Crear el path de la nueva carpeta si aún no existe
        target_directory = os.path.join(base_target_directory, code)
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        # Ruta completa del archivo fuente
        source_path = os.path.join(src_directory, filename)

        # Ruta completa del destino
        destination_path = os.path.join(target_directory, filename)

        # Mover el archivo
        shutil.move(source_path, destination_path)
        print(f"Moved {filename} to {destination_path}")

print("All images have been sorted.")
