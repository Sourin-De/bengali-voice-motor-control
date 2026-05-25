import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak...")
    try:
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    except:
        print("Timeout! No speech detected")
        exit()

try:
    text = r.recognize_google(audio, language="bn-IN")
    print("আপনি বললেন:", text)
except:
    print("Error! Could not understand audio")