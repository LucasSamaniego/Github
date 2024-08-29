import cv2
from pyzbar.pyzbar import decode
from PIL import Image
import numpy as np

def main():
    # Inicializa a câmera (0 é geralmente o índice para a câmera padrão do sistema)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro ao abrir a câmera.")
        return

    try:
        # Captura uma imagem da câmera
        ret, frame = cap.read()

        if not ret:
            print("Erro ao capturar imagem.")
            return

        # Converte a imagem de BGR (OpenCV) para RGB (PIL)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Converte a imagem para formato PIL
        image = Image.fromarray(frame_rgb)

        # Decodifica QR codes
        decoded_objects = decode(image)

        # Verifica se um QR code foi encontrado e imprime o resultado
        if decoded_objects:
            for obj in decoded_objects:
                print(f"QR Code Data: {obj.data.decode('utf-8')}")
        else:
            print("Nenhum QR code encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        # Libera os recursos da câmera
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
