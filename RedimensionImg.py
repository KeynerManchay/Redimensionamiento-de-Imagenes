import cv2
import os
import glob

# Definir el directorio donde están tus imágenes
input_directory = 'C:/Users/DELL/Desktop/DatasetSacos/Todo'
output_directory = 'C:/Users/DELL/Desktop/DatasetSacos/Images'

# Crear el directorio de salida si no existe
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Definir el nuevo tamaño deseado para YOLO
width = 640
height = 640
dim = (width, height)

# Obtener una lista de todas las imágenes en el directorio
image_paths = glob.glob(os.path.join(input_directory, '*'))

# Iterar sobre todas las imágenes
for image_path in image_paths:
    # Cargar la imagen
    image = cv2.imread(image_path)

    # Redimensionar la imagen
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # Construir el path de salida
    output_path = os.path.join(output_directory, os.path.basename(image_path))

    # Guardar la imagen redimensionada
    cv2.imwrite(output_path, resized_image)

print("Todas las imágenes han sido redimensionadas y guardadas en:", output_directory)
