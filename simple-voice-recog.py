import speech_recognition as sr


r = sr.Recognizer()
# Get audio from the microphone
with sr.Microphone(sample_rate=16000) as source:
    print("Please wait. I'm working with the mic...")
    # listen for 5 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)
    print("I'm ready :)")  
    audio = r.record(source, duration=5)  

# Recognize speech using Google (require internet)
try:
    print("I hear you saying:'" + r.recognize_google(audio) + "'")

except sr.UnknownValueError:
    print("I missed what you just said...")
except sr.RequestError as e:
    print("Opps, there's something wrong; {0}".format(e))