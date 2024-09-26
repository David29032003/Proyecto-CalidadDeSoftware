from unittest.mock import Mock
from typing import List, Tuple, Dict
import random

class CamaraSimulada:
    def __init__(self, url: str, id:    str, tipoCamara: str, coordenadas: Tuple[float, float]):
        self.url = url
        self.id = id
        self.tipo = tipoCamara
        self.coordenadas = coordenadas
        self.cuenta_frames = 0

    def TransmitirImagenes(self) -> List[Dict[str, str]]:
        imagenesSimuladas = []
        # Simulo 10 frames de imágenes como ejemplo
        #for i in range(10):
        estaOnline = self.estaOnline()  # Verifico si la cámara está activa

        frame = {
            'timestamp': f'2024-09-23 12:00', # Simulo los tiempos
            'datosImagen': f'datosFrame_{random.randint(0, 10)}', # Datos simulados
            'camaraOnline': estaOnline, # Estado de la cámara
            'personaDetectada': self.eventoAparicionPersona(estaOnline), # Verifico si el frame detecto a una persona
            'cocheDetectado': self.eventoAparicionCoche(estaOnline), # Verifico si el frame detecto a un coche
            'movimientoDetectado': self.eventoMovimiento(estaOnline) # Verifico si el frame detecto movimiento
        }

        return frame

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
                          f"Cámara online: {frame['camaraOnline']}, "
                          f"Persona detectada: {frame['personaDetectada']}, "
                          f"Coche detectado: {frame['cocheDetectado']}, "
                          f"Movimiento detectado: {frame['movimientoDetectado']}")
                break



