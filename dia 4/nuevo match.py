cliente = {"nombre ": "federico",
           "edad": 45,
           "ocupacion": "instructor"}

pelicula = {"titulo: "matrix",
            "ficha_tecnica": {"protagonista":"keanu reeves",
                             "director": "lana y lilly such"}}

elementos = [cliente,pelicula,"libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "ocupacion":ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {"titulo": titulo,
              "ficha_tecnica": {"protagonista":protagonista,
                                "director":director}}:
            print("es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("No se que es esto")