from .entidad_vineria import *
# from vino import *
import json


class Cepa(EntidadVineria):

    def __init__(self, id, nombre) -> None:
        super().__init__(id, nombre)
        
    # Comandos
    
    # Consultas
    
    def obtenerVinos(self)  : #-> list[Vino] #TODO
        pass

    def convertirAJSON(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})