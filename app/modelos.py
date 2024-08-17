from abc import ABC, abstractmethod
import csv


class Model(ABC):  # SE CREA LA INTERFAZ - HEREDA DE CLASE ABSTRACTA ABC
    @classmethod
    @abstractmethod  # EL ORDEN AL PARECER ES IMPORTANTE, DEBE IR DEBAJO DE CLASSMETHOD PARA QUE NO DE ERROR DE PYTEST
    def create_from_dict(cls, diccionario):
        pass


class Director:
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(diccionario["nombre"], int(diccionario["id"]))

    def __init__(self, nombre: str, id: int = -1):
        self.nombre = nombre
        self.id = id

    def __repr__(
        self,
    ) -> str:  # Devuelve una cadena que representa al objeto de manera oficial. Está destinado a ser un string que permita recrear el objeto.
        return f"Director ({self.id}): {self.nombre}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id and self.nombre == other.nombre
        return False

    def __hash__(self):
        return hash((self.id, self.nombre))


class Pelicula:
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(
            diccionario["titulo"],
            diccionario["sinopsis"],
            int(diccionario["director_id"]),
            int(diccionario["id"]),
        )

    def __init__(self, titulo: str, sinopsis: str, director: object, id=-1):
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.id = id
        self.director = director

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        if isinstance(value, Director):
            self._director = value
            self._id_director = value.id
        elif isinstance(value, int):
            self._director = None
            self._id_director = value
        else:
            raise TypeError(f"{value} debe ser un entero o instancia de Director")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                self.titulo == other.titulo
                and self.sinopsis == other.sinopsis
                and self.director == other.director
                and self.id == other.id
            )
        return False

    def __hash__(self):
        return hash((self.id, self.titulo, self.sinopsis, self.director))

    def __repr__(self):
        return f"Pelicula ({self.id}): {self.titulo}, {self.director}"


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


class DAO_CSV(DAO):  # ESTO SE HA QUITADO DE LAS SIGUIENTES CLASS 2 DE ABAJO
    model = None

    def __init__(self, path: str, encoding="utf-8"):
        self.path = path
        self.encoding = encoding

    def todos(self):
        # with open("data/directores.csv","r", newline= "") as fichero:
        with open(self.path, "r", encoding=self.encoding, newline="") as fichero:
            lector_csv = csv.DictReader(fichero, delimiter=";", quotechar="'")
            lista = []
            for registro in lector_csv:
                lista.append(self.model.create_from_dict(registro))
        return lista


class DAO_CSV_Director(DAO_CSV):
    """def todos(self):
    # with open("data/directores.csv","r", newline= "") as fichero:
    with open(self.path, "r", encoding="utf-8", newline="") as fichero:
        lector_csv = csv.DictReader(fichero, delimiter=";", quotechar="'")
        lista = []
        for registro in lector_csv:
            lista.append(Director.create_from_dict(registro))
    return lista"""

    model = Director


class DAO_CSV_Pelicula(DAO_CSV):
    """def todos(self):
    with open(self.path, "r", encoding="utf-8", newline="") as fichero:
        lector_csv = csv.DictReader(fichero, delimiter=";", quotechar="'")
        lista = []
        for registro in lector_csv:
            lista.append(Pelicula.create_from_dict(registro))
    return lista"""

    model = Pelicula
