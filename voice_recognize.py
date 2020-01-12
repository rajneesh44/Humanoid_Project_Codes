import speech_recognition as sr


# obtain audio from the microphone
r = sr.Recognizer()
mic = sr.Microphone(device_index = 1)


with mic as source:
    print("speak")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    if(audio):
        print("listening")
        if(audio=="exit"):
            exit()
    print(r.recognize_google(audio))
