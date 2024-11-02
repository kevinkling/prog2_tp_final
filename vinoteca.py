# librerias
import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class Vinoteca:

    __archivoDeDatos = "vinoteca.json"
    __bodegas: list[Bodega] = []
    __cepas: list[Cepa] = []
    __vinos: list[Vino] = []

    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)

    # Consultas
    
    def obtenerBodegas(orden=None, reverso=False) -> list[Bodega]:
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
            elif orden == "vinos":
                pass  # completar
        return Vinoteca.__bodegas

    def obtenerCepas(orden=None, reverso=False) -> list[Cepa]:
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
        return Vinoteca.__cepas


    def obtenerVinos(anio=None, orden=None, reverso=False) -> list[Vino]:
        if isinstance(anio, int):
            pass  # completar
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
            elif orden == "bodega":
                pass  # completar
            elif orden == "cepas":
                pass  # completar
        return Vinoteca.__vinos

    def buscarBodega(id:str): #PROBAR - 
        for bodega in Vinoteca.__bodegas :
            if bodega.obtenerId() == id :
                return bodega
        return None 

    def buscarCepa(id:str): #PROBAR - 
        for cepa in Vinoteca.__cepas :
            if cepa.obtenerId() == id :
                return cepa
        return None 

    def buscarVino(id):
        pass  # completar

    def __parsearArchivoDeDatos():
        # Abre el archivo JSON
        with open(Vinoteca.__archivoDeDatos, 'r', encoding='utf-8') as archivo:
            # Retorna el contenido del archivo JSON
            return json.load(archivo)

    def __convertirJsonAListas(lista):
        for bodega in lista["bodegas"] :
            Vinoteca.__bodegas.append(Bodega(bodega["id"], bodega["nombre"]))
        
        for cepa in lista["cepas"] :
            Vinoteca.__cepas.append(Cepa(cepa["id"], cepa["nombre"]))
        
        for vino in lista["vinos"] :
            Vinoteca.__vinos.append(Vino(vino["id"], vino["nombre"], vino["bodega"], vino["cepas"], vino["partidas"]))
