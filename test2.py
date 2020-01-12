import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index = 0)

with mic as source:
    print("speak")
    r.adjust_for_ambient_noise(source,duration=5)
    audio = r.listen(source)
    if(audio):
        print("listening")
        if(audio == "exit"):
            exit()
    print(r.recognize_google(audio))

