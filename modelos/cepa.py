from .entidad_vineria import *
# from vino import *
import json
import vinoteca


class Cepa(EntidadVineria):

    def __init__(self, id, nombre) -> None:
        super().__init__(id, nombre)
        
    # Comandos
    
    # Consultas
    
    def obtenerVinos(self)  : #-> list[Vino] #TODO
        todos_los_vinos = vinoteca.Vinoteca.obtenerVinos()
        vinos_pertenece = []
        for vino in todos_los_vinos :
            for cepa in vino.obtenerCepas() :
                if cepa.obtenerVinos() == self.obtenerId() :
                    vinos_pertenece.append(vino)
        return vinos_pertenece
        

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