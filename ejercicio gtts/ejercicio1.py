from gtts import gTTS
tts = gTTS ("Hola, este es mi primer programa hablando en Python", lang='es')
tts.save("saludo.mp3")