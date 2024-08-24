from picamera2 import Picamera2
import cv2

# Inicializa a câmera
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())

# Inicia a câmera
picam2.start()

# Captura uma imagem da câmera
frame = picam2.capture_array()

# Converte a imagem para escala de cinza
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Inicializa o detector de QR code
qrCodeDetector = cv2.QRCodeDetector()

# Detecta e decodifica o QR code
data, points, _ = qrCodeDetector.detectAndDecode(gray)

# Verifica se um QR code foi encontrado e imprime o resultado
if data:
    print(f"QR Code Data: {data}")
else:
    print("Nenhum QR code encontrado.")

# Libera os recursos da câmera
picam2.stop()
