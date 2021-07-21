from playsound import playsound
from gtts import gTTS

mytext = 'Hello!! Welcome to Blue Learn Open Sauce'
language = 'en'
speech = gTTS(text=mytext, lang=language, slow=False)
speech.save("hello.mp3")
playsound('hello.mp3')
