

def encriptador(texto):
    # Recibe una cadena de texto y la encripta para que no pueda ser leída.

    texto_final=''
    
    for letra in texto:
        ascci = ord(letra)
        ascci += 7
        texto_final += chr(ascci)

    return texto_final

def desencriptador(texto):
    # Recibe una cadena de texto encriptada y la desencripta para que se pueda leer.

    texto_final = ''

    for letra in texto:
        ascci = ord(letra)
        ascci -= 7
        texto_final += chr(ascci)

    return texto_final




texto = input("Ingrese un texto: ")

texto_encriptado = encriptador(texto)
texto_desencriptado = desencriptador(texto_encriptado)

print("Texto original: " + texto)
print("Texto encriptado: " + texto_encriptado)
print("Texto desencriptado: " + texto_desencriptado)