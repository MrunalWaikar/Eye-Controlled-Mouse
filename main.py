import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Please speak...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_sphinx(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError:
    print("Sphinx error.")

