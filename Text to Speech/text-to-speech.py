from playsound import playsound
from gtts import gTTS

mytext=input("Enter Text : ")
language = 'en'
speech = gTTS(text=mytext, lang=language, slow=False)
speech.save("hello.mp3")
playsound('hello.mp3')
