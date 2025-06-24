import sys
import os
import folium
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Localização inicial do mapa (ex: São Paulo)
latitude, longitude = -23.5505, -46.6333

# Cria o mapa com folium
mapa = folium.Map(location=[latitude, longitude], zoom_start=13)

# Adiciona um marcador
folium.Marker(
    location=[latitude, longitude],
    popup="Você está aqui!",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mapa)

# Salva como HTML
mapa.save("mapa.html")

# Cria janela com PyQt
class JanelaMapa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mapa Interativo - Etapa 1")
        self.setGeometry(100, 100, 800, 600)

        navegador = QWebEngineView()
        caminho_html = os.path.abspath("mapa.html")
        navegador.load(f"file:///{mapa.html}")

        self.setCentralWidget(navegador)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaMapa()
    janela.show()
    sys.exit(app.exec_())