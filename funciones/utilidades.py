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
        print('Respuesta inválida. Ingresa "s" para sí o "n" para no.')

def verificar_string(texto):
    try:
        if any(caracter.isdigit() for caracter in texto):
            raise ValueError('El campo no puede contener números')
        return True
    except ValueError as e:
        print(f'AVISO: {e}. Intente nuevamente')
        return False