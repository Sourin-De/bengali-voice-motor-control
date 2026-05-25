import speech_recognition as sr

action_on = ["চালু", "অন", "শুরু", "ঘোরাও"]
action_off = ["বন্ধ", "অফ"]

devices = {
    "motor": ["মোটর"],
    "fan": ["পাখা", "ফ্যান"],
    "light": ["আলো", "লাইট"]
}

def understand(text):
    action = None
    device = None

    for word in action_on:
        if word in text:
            action = "on"
            break

    for word in action_off:
        if word in text:
            action = "off"
            break

    for dev, words in devices.items():
        for w in words:
            if w in text:
                device = dev
                break

    if action and device:
        print(f"Device: {device.capitalize()} -> Turned {action.upper()}")
        return {"device": device, "action": action}

    else:
        print("Could not understand command.")
        return None


r = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting noise...")
    r.adjust_for_ambient_noise(source,duration=1)

    print("Speak...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio,language="bn-IN")

    print("You said:", text)

    understand(text)

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError:
    print("API error")