from modelos.entidad_vineria import EntidadVineria
# from .bodega import *
# from .cepa import *
import json
import vinoteca


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

    def obtenerBodega(self)  : #NOTE - LISTO -> Bodega
        return vinoteca.Vinoteca.buscarBodega(self.__bodega)
    
    def obtenerCepas(self)  : #-> list[Cepa] # PROBAR -> list[Cepa]
        todas_las_cepas = vinoteca.Vinoteca.obtenerCepas()
        cepas = []
        
        for cepa in todas_las_cepas :
            for cepaID in self.__cepas :
                if cepa.obtenerId() == cepaID :
                    cepas.append(cepa)
        return cepas
    
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