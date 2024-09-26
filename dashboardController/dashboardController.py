from dataclasses import dataclass
from typing import Tuple

class ObjectType:
    CAMERA = 'CAMERA'
    PROXIMITY_SENSOR = 'PROXIMITY_SENSOR'
    SERVO = 'SERVO'


@dataclass
class ExternalObject:
    urlAddress: str
    gpsCoordinates: Tuple[float, float]
    typeObject: ObjectType.CAMERA
    idObject: int = -1
    
class DashboardController:
    def __init__(self):
        self.objectList = {}

    def addObj(self, externalObject):
        if externalObject.idObject == -1:
            self.objectList[externalObject.idObject] = externalObject
        else:
            self.objectList[externalObject.idObject] = externalObject
            
    def removeObj(self, idObject : int):
        if idObject in [ids.id for ids in self.objectList]:
            del self.objectList[idObject]
    def getConfig(self):
        return self.objectList



