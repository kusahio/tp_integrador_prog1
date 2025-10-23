import unicodedata


def quitar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def preguntar_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ('s', 'n'):
            return respuesta == 's'
        print('Respuesta inválida. Ingrese "s" para sí o "n" para no.')