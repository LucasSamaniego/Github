from picamera2 import Picamera2
from pyzbar.pyzbar import decode
from PIL import Image
import numpy as np

# Inicializa a câmera
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())

# Inicia a câmera
picam2.start()

try:
    # Captura uma imagem da câmera
    frame = picam2.capture_array()

    # Converte a imagem para formato PIL
    image = Image.fromarray(frame)

    # Decodifica QR codes
    decoded_objects = decode(image)

    # Verifica se um QR code foi encontrado e imprime o resultado
    if decoded_objects:
        for obj in decoded_objects:
            print(f"QR Code Data: {obj.data.decode('utf-8')}")
    else:
        print("Nenhum QR code encontrado.")

finally:
    # Garante que os recursos da câmera sejam liberados
    picam2.stop()
