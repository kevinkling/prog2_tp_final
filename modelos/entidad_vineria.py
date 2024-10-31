from abc import ABC, abstractmethod

class EntidadVineria(ABC) :
    
    @abstractmethod
    def __init__(self, id, nombre) -> None:
        self.__id: str = id
        self.__nombre: str = nombre
        
        
    # Comandos
    
    
    def establecerNombre(self, nombre: str) -> None :
        self.__nombre = nombre
        
    # Consultas
    
    def obtenerId(self) -> str :
        return self.__id 
    
    def obtenerNombre(self) -> str :
        return self.__nombre
    
    # @abstractmethod
    # def descripcion(self) -> str:
    #     """Método abstracto que obliga a las subclases a proporcionar una descripción."""
    #     pass
    
    def __eq__(self, value: object) -> bool: #PROBAR - probar esto
        if isinstance(value, EntidadVineria) :
            return self.__id == value.__id
        return False # Devuelve False si 'value' no es una instancia de EntidadVineria