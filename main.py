import networkx as nx
import cv2
from pyzbar.pyzbar import decode

# Função para determinar a direção com base nas coordenadas
def calcular_direcao(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    if abs(dx) > abs(dy):
        return "Direita" if dx > 0 else "Esquerda"
    else:
        return "Frente" if dy > 0 else "Tras"

# Função para ler e decodificar o QR Code usando OpenCV e Pyzbar
def ler_qr_code(frame):
    qr_codes = decode(frame)
    for qr_code in qr_codes:
        data = qr_code.data.decode('utf-8')
        return data
    return None

# Função para calcular a direção do próximo passo
def calcular_direcoes(G, pos_usuario, destino):
    shortest_path = nx.shortest_path(G, source=pos_usuario, target=destino, weight='weight')
    if len(shortest_path) < 2:
        return "Destino já alcançado ou caminho invalido"
    nodo_atual = shortest_path[0]
    nodo_proximo = shortest_path[1]
    direcao = calcular_direcao(nodos[nodo_atual], nodos[nodo_proximo])
    return direcao

# Criando um grafo
G = nx.Graph()

# Adicionando nodos ao grafo com coordenadas (x, y)
nodos = {
    "Entrada": (0, 0),
    "Corredor1": (5, 0),
    "Corredor2": (10, 0),
    "SalaA": (5, 5),
    "SalaB": (10, 5)
}

for nodo, pos in nodos.items():
    G.add_node(nodo, pos=pos)

# Adicionando arestas manualmente conforme a primeira versão
arestas = [
    ("Entrada", "Corredor1"),
    ("Corredor1", "Corredor2"),
    ("Corredor1", "SalaA"),
    ("Corredor2", "SalaB")
]

for aresta in arestas:
    nodo1, nodo2 = aresta
    G.add_edge(nodo1, nodo2, weight=5)

# Variável para rastrear a última posição do usuário
ultima_posicao = None

# Captura de vídeo da câmera
cap = cv2.VideoCapture(0, cv2.CAP_V4L)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Lendo o QR Code
    pos_usuario = ler_qr_code(frame)

    if pos_usuario in G.nodes:
        if pos_usuario != ultima_posicao:
            print(f"\nPosicao atual do usuario: {pos_usuario}")
            
            # Calculando a próxima direção a ser seguida
            proxima_direcao = calcular_direcoes(G, pos_usuario, "SalaB")
            #print("Próxima direção a seguir:")
            print(proxima_direcao)

            # Atualizando a última posição
            ultima_posicao = pos_usuario

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
