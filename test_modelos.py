import unittest
from unittest.mock import patch

from modelos import CamaraSimulada


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


    




if __name__ == '__main__':
    unittest.main()
