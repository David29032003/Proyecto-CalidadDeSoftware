import unittest
from unittest.mock import patch, Mock
from modelos import CamaraSimulada, PanelDeControl, ControladorCamara, ControladorVista


class TestCamaraSimulada(unittest.TestCase):

    def setUp(self):
        self.camara_simulada = CamaraSimulada("rtsp://ejemplo.com/canal/1", "7985462", "VisionNocturna", (24.434, 33.339))

    # Probamos cuando la camara esta online y random.choice devuelve True
    @patch('random.choice', return_value=True)
    def test_eventoAparicionPersona_online(self, mock_random_choice):
        esta_online = True
        resultado = self.camara_simulada.eventoAparicionPersona(esta_online)
        self.assertTrue(resultado)

    # Probamos cuando la cámara está offline y random.choice devuelve False
    @patch('random.choice', return_value=False)
    def test_eventoAparicionPersona_offline(self, mock_random_choice):
        esta_online = False
        resultado = self.camara_simulada.eventoAparicionPersona(esta_online)
        self.assertFalse(resultado)

    # Probamos cuando la cámara está online y random.choice devuelve True
    @patch('random.choice', return_value=True)
    def test_eventoAparicionCoche_online(self, mock_random_choice):
        esta_online = True
        resultado = self.camara_simulada.eventoAparicionCoche(esta_online)
        self.assertTrue(resultado)

    # Probamos cuando la cámara está online y random.choice devuelve False
    @patch('random.choice', return_value=False)
    def test_eventoMovimiento_online(self, mock_random_choice):
        esta_online = True
        resultado = self.camara_simulada.eventoMovimiento(esta_online)
        self.assertFalse(resultado)

    # Probamos si random.choice está devolviendo True para estaOnline
    @patch('random.choice', return_value=True)
    def test_estaOnline(self, mock_random_choice):
        resultado = self.camara_simulada.estaOnline()
        self.assertTrue(resultado)

    def test_TransmitirImagenes(self):
        # Probamos que el método TransmitirImagenes devuelva 10 frames
        frames = self.camara_simulada.TransmitirImagenes()
        # se genera 10 frames
        self.assertEqual(len(frames), 10)

        # Probamos que cada frame tenga las claves correctas
        for frame in frames:
            self.assertIn('numeroFrame', frame)
            self.assertIn('timestamp', frame)
            self.assertIn('datosImagen', frame)
            self.assertIn('personaDetectada', frame)
            self.assertIn('camaraOnline', frame)
            self.assertIn('cocheDetectado', frame)
            self.assertIn('movimientoDetectado', frame)


class TestCamarasSimuladas(unittest.TestCase):
    @patch('random.choice', side_effect=[False] * 10)
    def test_perdida_conexion_con_camaras(self, mock_random_choice):
        # Configuramos la cámara simulada
        camara_simulada = CamaraSimulada(url="http://camara2", id="cam2", tipoCamara="tipo2", coordenadas=(15.0, 25.0))
        controlador_vista = ControladorVista()

        # Obtenemos los frames simulados (en este caso todas las cámaras estarán offline)
        frames_simulados = camara_simulada.TransmitirImagenes()

        # Establecemos los datos en el visor de la cámara
        controlador_vista.establecerDatos(frames_simulados)

        # Creamos un panel de control con una cámara y un visor
        panel = PanelDeControl(
            camaras=[ControladorCamara("http://camara2", "cam2", "tipo2", (15.0, 25.0))],
            visoresPorCamara=[controlador_vista],
            tamanoDisco="500GB"
        )

        # Validamos que el panel muestra la transmisión con todas las cámaras offline
        panel.mostrarTransmisionDeCamara("cam2")

        # Comprobamos que todos los frames tengan la cámara en estado offline
        for frame in frames_simulados:
            self.assertFalse(frame['camaraOnline'])

    # @patch('random.choice', side_effect=[False, False, True, True, False, False, True, True, False, False])
    # @patch.object(CamaraSimulada, 'eventoAparicionPersona',
    #               side_effect=[False, False, True, False, False, False, True, False, False, False])  # Mock eventoAparicionPersona
    # @patch.object(CamaraSimulada, 'eventoAparicionCoche',
    #               side_effect=[False, False, False, True, False, False, False, True, False, False])  # Mock eventoAparicionCoche
    # @patch.object(CamaraSimulada, 'eventoMovimiento',
    #               side_effect=[False, False, False, False, False, False, False, False, False, False])  # Mock eventoMovimiento
    @patch.object(CamaraSimulada, 'estaOnline', side_effect=[False, False, True, True, False, False, True, True, False, False])  # Mock estaOnline (cada vez que se llame a este método devuelve sideeffect)
    def test_reconexion_de_camaras_perdidas(self,mock_esta_online):
        # Configuramos la cámara simulada
        camara_simulada = CamaraSimulada(url="http://camara3", id="cam3", tipoCamara="tipo3", coordenadas=(20.0, 30.0))
        controlador_vista = ControladorVista()

        # Obtenemos los frames simulados
        frames_simulados = camara_simulada.TransmitirImagenes()

        # Establecemos los datos en el visor de la cámara
        controlador_vista.establecerDatos(frames_simulados)

        # Creamos un panel de control con una cámara y un visor
        panel = PanelDeControl(
            camaras=[ControladorCamara("http://camara3", "cam3", "tipo3", (20.0, 30.0))],
            visoresPorCamara=[controlador_vista],
            tamanoDisco="500GB"
        )

        # Validamos que el panel muestra la transmisión con reconexiones
        panel.mostrarTransmisionDeCamara("cam3")

        # Comprobamos que los frames alternen entre offline y online
        for i, frame in enumerate(frames_simulados):
            if i % 4 < 2:  # Los primeros dos frames de cada bloque de 4 son offline
                self.assertFalse(frame['camaraOnline'])
            else:  # Los dos siguientes son online
                self.assertTrue(frame['camaraOnline'])

    @patch.object(CamaraSimulada, 'estaOnline', side_effect=[True] * 10)  # Mock estaOnline (siempre online)
    @patch.object(CamaraSimulada, 'eventoAparicionPersona', side_effect=[True if i % 2 == 0 else False for i in range(10)])  # True en frames impares
    def test_detecion_persona_en_frames_impares(self, mock_evento_persona, mock_esta_online):
        # Configuramos la cámara simulada
        camara_simulada = CamaraSimulada(url="http://camara3", id="cam3", tipoCamara="tipo3",
                                         coordenadas=(20.0, 30.0))
        controlador_vista = ControladorVista()

        # Obtenemos los frames simulados
        frames_simulados = camara_simulada.TransmitirImagenes()

        # Establecemos los datos en el visor de la cámara
        controlador_vista.establecerDatos(frames_simulados)

        # Creamos un panel de control con una cámara y un visor
        panel = PanelDeControl(
            camaras=[ControladorCamara("http://camara3", "cam3", "tipo3", (20.0, 30.0))],
            visoresPorCamara=[controlador_vista],
            tamanoDisco="500GB"
        )

        # Validamos que el panel muestra la transmisión con reconexiones
        panel.mostrarTransmisionDeCamara("cam3")

        # Verificamos si en los frames impares se detectó a una persona
        for i, frame in enumerate(frames_simulados):
            if i % 2 != 0:  # Frames pares
                self.assertFalse(frame['personaDetectada'],
                                 f"Se detectó una persona en el frame {i + 1}, que es un frame impar.")
            else:  # Frames impares
                self.assertTrue(frame['personaDetectada'],
                                f"No se detectó una persona en el frame {i + 1}, que es un frame par.")


if __name__ == '__main__':
    unittest.main()
