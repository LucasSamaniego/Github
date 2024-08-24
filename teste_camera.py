import cv2
from picamera2 import Picamera2

# Inicializar a câmera
picam2 = Picamera2()
picam2.start()

# Capturar imagem
frame = picam2.capture_array()

# Exibir a imagem capturada (opcional)
cv2.imshow("Imagem Capturada", frame)
cv2.waitKey(0)  # Pressione qualquer tecla para fechar a janela

# Salvar a imagem capturada
cv2.imwrite("foto.jpg", frame)

# Liberar a câmera e fechar janelas
picam2.close()
cv2.destroyAllWindows()
