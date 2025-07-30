# contador.py

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

# Prueba rápida
if __name__ == "__main__":
    entrada = input("Escribe una frase: ")
    resultado = contar_palabras(entrada)
    print("Número de palabras:", resultado)
