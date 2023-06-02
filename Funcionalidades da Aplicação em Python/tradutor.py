
from translate import Translator
import translate
import gtts
from playsound import playsound
from langdetect import detect

frase = input("Frase: ")
idioma = input("Idioma: ")

def traduzir():
    #detecta de qual lingua pertence essa frase
    lang_detected = detect(frase)
    print(lang_detected)
    #passa os parametros da linha que será traduzida para a que se quer traduzir
    s=Translator(from_lang=lang_detected, to_lang=idioma)
    #traduz a frase
    res = s.translate(frase)
    print(s.from_lang, s.to_lang)
    #imprime a mensagem traduzida
    return res
    #passa os parametros para o audia...

print(traduzir())