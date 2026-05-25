import speech_recognition as sr

action_on = ["চালু", "অন", "শুরু", 
             "ঘোরাও","জ্বালাও","জ্বালাবে","জ্বালিয়ে",
             "চালু", "চালিয়ে", "চালাবে", "চালাও"]

action_off = ["বন্ধ", "অফ",
            "বন্ধ করো", "বন্ধ করে দাও",
            "থামাও", "নিভাও"]

devices = {
    "motor": ["মোটর"],
    "fan": ["পাখা", "ফ্যান", "ফ্যানটা","প্যান", "প্যানটা",
        "গ্যান", "পান"],
    "light": ["আলো", "লাইট", "বাতি", "লাইটটা"]
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
        if any(w in text for w in words):
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