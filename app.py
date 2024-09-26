from modelos import CamaraSimulada, ControladorCamara, ControladorVista, PanelDeControl

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

