from flask import Flask, jsonify, request
from dashboardController import DashboardController, ObjectType, ExternalObject

app = Flask(__name__)


controller = DashboardController()
object1 = ExternalObject(
    urlAddress="https://example.com/camara1",
    gpsCoordinates=(10.2345, -5.6789),
    typeObject=ObjectType.CAMERA,
    idObject=123
)
object2 = ExternalObject(
    urlAddress="https://example.com/camara2",
    gpsCoordinates=(10.2345, -5.6789),
    typeObject=ObjectType.CAMERA,
    idObject=456
)
controller.addObj(object1)
controller.addObj(object2)
@app.route('/get-config', methods=['GET'])
def get_config():

    configJson = controller.getConfig()
    print(configJson)
    return jsonify(configJson)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')