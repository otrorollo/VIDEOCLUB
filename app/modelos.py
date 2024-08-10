from abc import ABC, abstractmethod
import csv


class Director:
    def __init__(self, nombre: str, id: int = -1):
        self.nombre = nombre
        self.id = id
    def __repr__(self) -> str: #Devuelve una cadena que representa al objeto de manera oficial. Está destinado a ser un string que permita recrear el objeto.
        return f"Director ({self.id}): {self.nombre}"
    def __eq__(self, value: object) -> bool: #Define el comportamiento del operador de igualdad (==). Compara dos objetos para determinar si son iguales.
        pass


class DAO(ABC):
    """
    #def __init__(self, *args)
        #raise NotImplementedError("No se debe usar DAO, es una interfaz")
    @abstractmethod #decorador
    def guardar(self, instancia):
      pass
      #raise NotImplementedError("No se debe usar DAO, es una interfaz")
    @abstractmethod
    def actualizar(self, instancia):
      pass
      #raise NotImplementedError("No se debe usar DAO, es una interfaz")
    @abstractmethod
    def borrar(self, instancia):
      pass
      #raise NotImplementedError("No se debe usar DAO, es una interfaz")
    @abstractmethod
    def consultar(self, instancia):
      pass
      #raise NotImplementedError("No se debe usar DAO, es una interfaz")
    """

    @abstractmethod
    def todos(self):
        pass
        # raise NotImplementedError("No se debe usar DAO, es una interfaz")


class DAO_CSV_Director(DAO):
    def __init__(self, path):  # path es la ruta que abre el csv
        self.path = path

    def todos(self):
        # with open("data/directores.csv","r", newline= "") as fichero:
        with open(self.path, "r", newline="") as fichero:
            lector_csv = csv.DictReader(fichero, delimiter=";", quotechar="'")
            lista = []
            for registro in lector_csv:
                lista.append(Director(registro["nombre"], registro["id"]))
        return lista
