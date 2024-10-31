from .entidad_vineria import *
# from .bodega import *
# from .cepa import *
import json


class Vino(EntidadVineria):

    def __init__(self, id:str, nombre:str, bodega:str, cepas:list[str], partidas:list[int]) -> None:
        super().__init__(id, nombre)
        self.__bodega : str = bodega # bodegaID
        self.__cepas : list[str] = cepas # cepasIDs
        self.__partidas : list[int] = partidas
        
    # Comandos
    
    def establecerBodega(self, bodega:str) :
        self.__bodega = bodega
        
    def establecerCepas(self, cepas:list[str]) :
        self.__cepas = cepas
        
    def establecerPartidas(self, partidas:list[int]) :
        self.__partidas = partidas
    
    # Consultas

    def obtenerBodega(self)  :#-> Bodega #TODO
        pass
    
    def obtenerCepas(self)  : #-> list[Cepa] #TODO
        pass
    
    def obtenerPartidas(self) -> list[int] :
        return self.__partidas

    def convertirAJSON(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def convertirAJSONFull(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})