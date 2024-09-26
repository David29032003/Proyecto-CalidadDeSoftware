from flask import Flask, jsonify, request
from modelos import CamaraSimulada

app = Flask(__name__)

camaraSimulada = CamaraSimulada("rtsp://ejemplo.com/canal/1", "7985462", "VisionNocturna", (24.434, 33.339))


@app.route('/get_frames', methods=['GET'])
def get_frames():
    datosTransmision = camaraSimulada.TransmitirImagenes()
    return jsonify(datosTransmision)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')