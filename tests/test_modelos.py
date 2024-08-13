from app.modelos import Director, DAO_CSV_Director, Pelicula


def test_create_director():
    # Cuando se crea un nuevo Director, si no se especifica un id, se asigna -1 por defecto
    # se conoce tambien como Placeholder
    director = Director("Robert Redford")

    assert director.nombre == "Robert Redford"
    assert (
        director.id == -1
    )  # se usa para representar un id que aún no ha sido asignado


def test_dao_directores_traer_todos():
    dao = DAO_CSV_Director("tests/data/directores.csv")
    directores = dao.todos()

    assert len(directores) == 8
    assert directores[7] == Director("Charlie Chaplin", 8)


def test_create_pelicula():
    pelicula = Pelicula("El señor de los anillos", "Sauron es muy malo", 9)

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es muy malo"
    assert pelicula._id_director == 9
    assert (
        pelicula.id == -1
    )  # se usa para representar un id que aún no ha sido asignado
    assert (
        pelicula.director is None
    )  # es un operador de comparación, aqui preguntas de identidad


def test_create_pelicula_and_informar_director_completo():
    director = Director("Peter Jackson", 9)
    pelicula = Pelicula("El señor de los anillos", "Sauron es muy malo", director)

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es muy malo"
    assert pelicula._id_director == 9
    assert pelicula.id == -1
    assert pelicula.director == director


def test_asigna_director_a_pelicula():
    pelicula = Pelicula("El señor de los anillos", "Sauron es muy malo", -1)

    director = Director("Peter Jackson", 9)

    pelicula.director = director

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es muy malo"

    assert pelicula.id == -1
    assert pelicula.director == director
    assert pelicula._id_director == 9
