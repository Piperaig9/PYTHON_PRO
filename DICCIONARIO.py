
meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "GG": "Buen juego",
    "GOAT": "El mejor de todos los tiempos",
    "OMG": "Dios mio",
    }
palabra = input("Escribe una palabra que no entiendas")

if palabra in meme_dict.keys():
    print(meme_dict[palabra])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print("Lo siento esa palabra no esta en el diccionario")
    # ¿Qué hacer si no se encuentra la palabra?
