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
        bodegas = Vinoteca.__bodegas.copy() # Hago una copia (tambien sirve [:]) de la lista para no tocar la original
        if isinstance(orden, str):
            if orden == "nombre":
                bodegas.sort(key=lambda nombre: nombre.obtenerNombre()) # Uso una lambda para ordenar por el atributo nombre
            elif orden == "vinos":
                bodegas.sort(key=lambda bodega: len(bodega.obtenerVinos()))  # Uso una lambda para ordenar por la cantidad de vinos
        if reverso :
            bodegas.reverse()
        
        return bodegas 

    def obtenerCepas(orden=None, reverso=False) -> list[Cepa]:
        cepas = Vinoteca.__cepas.copy()
        if isinstance(orden, str):
            if orden == "nombre":
                cepas.sort(key=lambda cepa: cepa.obtenerNombre())
        if reverso :
            cepas.reverse()
            
        return cepas

    def obtenerVinos(anio=None, orden=None, reverso=False) -> list[Vino]:
        vinos = []
        if isinstance(anio, int):
            for vino in Vinoteca.__vinos :
                if anio in vino.obtenerPartidas() :
                    vinos.append(vino)
        else :
            vinos = Vinoteca.__vinos.copy()

        if isinstance(orden, str):
            if orden == "nombre":
                vinos.sort(key=lambda nombre: nombre.obtenerNombre())
            elif orden == "bodega":
                vinos.sort(key=lambda bodega: bodega.obtenerBodega().obtenerNombre())
            elif orden == "cepas":
                vinos.sort(key=lambda vino: len(vino.obtenerCepas()))
        
        if reverso :
            vinos.reverse()
        
        return vinos

    def buscarBodega(id:str) -> Bodega:
        for bodega in Vinoteca.__bodegas :
            if bodega.obtenerId() == id :
                return bodega
        return None 

    def buscarCepa(id:str) -> Cepa:
        for cepa in Vinoteca.__cepas :
            if cepa.obtenerId() == id :
                return cepa
        return None 

    def buscarVino(id) -> Vino:
        for vino in Vinoteca.__vinos :
            if vino.obtenerId() == id :
                return vino
        return None 

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
