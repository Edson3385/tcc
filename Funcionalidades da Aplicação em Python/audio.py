import gtts
from playsound import playsound
import speech_recognition as sr

rec = sr.Recognizer()
print(sr.Microphone().list_microphone_names())
with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    gravar = input(str('Deseja gravar o áudio?'))
    if gravar == 'sim':
       print('gravando...')
       audio = rec.listen(mic)
       with open('testeaudio.wav', 'wb') as f:
           f.write(audio.get_wav_data())
       
       texto = rec.recognize_google(audio, language='pt-br')
       print(texto)
       playsound('testeaudio.wav')