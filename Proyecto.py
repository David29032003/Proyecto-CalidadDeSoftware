from unittest.mock import Mock
from typing import List, Tuple, Dict
import random

class CamaraSimulada:
    def __init__(self, url: str, id: str, tipoCamara: str, coordenadas: Tuple[float, float]):
        self.url = url
        self.id = id
        self.tipo = tipoCamara
        self.coordenadas = coordenadas
        self.cuenta_frames = 0

    def TransmitirImagenes(self) -> List[Dict[str, str]]:
        imagenesSimuladas = []
        # Simulo 10 frames de imágenes como ejemplo
        for i in range(10):
            estaOnline = self.estaOnline()  # Verifico si la cámara está activa
            
            frame = {
                'numeroFrame': str(i + 1),
                'timestamp': f'2024-09-23 12:00:{10 + i}', # Simulo los tiempos
                'datosImagen': f'datosFrame_{i + 1}', # Datos simulados
                'personaDetectada': self.eventoAparicionPersona(estaOnline), # Verifico si el frame detecto a una persona
                'camaraOnline': estaOnline, # Estado de la cámara
                'cocheDetectado': self.eventoAparicionCoche(estaOnline), # Verifico si el frame detecto a un coche
                'movimientoDetectado': self.eventoMovimiento(estaOnline) # Verifico si el frame detecto movimiento
            }
            imagenesSimuladas.append(frame)
        return imagenesSimuladas

    def eventoAparicionPersona(self, estaOnline: bool) -> bool:
        # Verifico si la camara estaba online 
        if not estaOnline:
            return False
        # De manera aleatoria asigno True o False a este campo de los frames
        return random.choice([True, False])

    def estaOnline(self) -> bool:
        # De manera aleatoria asigno True o False a este campo de los frames
        return random.choice([True, False])

    def eventoAparicionCoche(self, estaOnline: bool) -> bool:
        # Verifico si la camara estaba online 
        if not estaOnline:
            return False
        # De manera aleatoria asigno True o False a este campo de los frames
        return random.choice([True, False])

    def eventoMovimiento(self, estaOnline: bool) -> bool:
        # Verifico si la camara estaba online 
        if not estaOnline:
            return False
        # De manera aleatoria asigno True o False a este campo de los frames
        return random.choice([True, False])


class ControladorCamara:
    def __init__(self, url: str, id: str, tipoCamara: str, coordenadas: Tuple[float, float]):
        self.url = url
        self.id = id
        self.tipo = tipoCamara
        self.coordenadas = coordenadas


class ControladorVista:
    def __init__(self):
        self.datos = []

    def establecerDatos(self, datos: List[Dict[str, str]]):
        self.datos = datos


class PanelDeControl:
    def __init__(self, camaras: List[ControladorCamara], visoresPorCamara: List[ControladorVista], tamanoDisco: str):
        self.camaras = camaras
        self.visores_por_camara = visoresPorCamara
        self.tamano_disco = tamanoDisco

    def mostrarTransmisionDeCamara(self, idCamara: str):
        for i, camara in enumerate(self.camaras):
            if camara.id == idCamara:
                transmision = self.visores_por_camara[i].datos
                print(f"Mostrando transmisión de la cámara {camara.id} en el visor {i}:")
                for frame in transmision:
                    print(f"Frame: {frame['numeroFrame']}, Timestamp: {frame['timestamp']}, Datos: {frame['datosImagen']}, "
                          f"Persona detectada: {frame['personaDetectada']}, "
                          f"Cámara online: {frame['camaraOnline']}, "
                          f"Coche detectado: {frame['cocheDetectado']}, "
                          f"Movimiento detectado: {frame['movimientoDetectado']}")
                break


if __name__ == "__main__":
    # Realizo una instancia para simular una camara
    camaraSimulada = CamaraSimulada("rtsp://ejemplo.com/canal/1", "7985462", "VisionNocturna", (24.434, 33.339))
    datosTransmision = camaraSimulada.TransmitirImagenes()

    # Creo un objeto de la clase ControladorVista
    controlador_vista = ControladorVista()
    controlador_vista.establecerDatos(datosTransmision)

    # Realizo una instancia para el controlador de la camara
    controlador_camara = ControladorCamara("rtsp://ejemplo.com/canal/1", "7985462", "VisionNocturna", (24.434, 33.339))

    # Realizo una instancia para el panel de control
    panel_de_control = PanelDeControl([controlador_camara], [controlador_vista], "5Tb")

    # Muestro la transmisión de la camara
    panel_de_control.mostrarTransmisionDeCamara("7985462")
