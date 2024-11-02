from modelos.entidad_vineria import EntidadVineria
# from .vino import Vino
# from modelos.cepa import *
# from vinoteca import Vinoteca
import vinoteca

import json


class Bodega(EntidadVineria):

    def __init__(self, id, nombre) -> None:
         super().__init__(id, nombre)
         
    # Comandos
    
    # Consultas
    
    def obtenerVinos(self)  : #-> list[Vino] 
        """ Vinos que estan en la bodega """
        todos_los_vinos = vinoteca.Vinoteca.obtenerVinos()
        vinos_pertenece = []
        for vino in todos_los_vinos :
            if vino.obtenerBodega().obtenerId() == self.obtenerId() :
                vinos_pertenece.append(vino)
        return vinos_pertenece
    
    def obtenerCepas(self)  : #-> list[Cepa]
        """ Cepas que estan en la bodega """
        cepas_pertenece = []
        for vino in self.obtenerVinos() :
            for cepa in vino.obtenerCepas() :
                if cepa not in cepas_pertenece :
                   cepas_pertenece.append(cepa)
        return cepas_pertenece
    
    def convertirAJSON(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        print(cepas)
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)

    def __repr__(self):
            return json.dumps(self.convertirAJSON())