# contador.py
def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def contar_caracteres(texto):
    return len(texto)

# Prueba rápida
if __name__ == "__main__":
    entrada = input("Escribe una frase: ")
    print("Número de palabras:", contar_palabras(entrada))
    print("Número de caracteres:", contar_caracteres(entrada))
