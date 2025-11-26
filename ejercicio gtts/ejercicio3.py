from gtts import gTTS
def mensaje_personalizado(texto, idioma='es', lento=False, tld='com', nombre='personalizado.mp3'):
    tts = gTTS (text=texto, lang=idioma, slow=lento, tld=tld)
    tts.save(nombre)
    print(f'Archivo generado: {nombre}')
    return nombre


texto_usuario = 'Hola, este es un mensaje personalizado generado con gTTS en Python.'
mensaje_personalizado(texto_usuario, idioma='es', lento=False, tld='com', nombre='mensaje_personalizado.mp3')