import speech_recognition as sr


def detectEndWords(s):
    end_words = ['okay then', 'okay Mom', 'okay done']
    for word in end_words:
        if (s.find(word) != -1):
            return True

    return False


r = sr.Recognizer()
context = ""
# Get audio from the microphone (16kHz)
with sr.Microphone(sample_rate=16000) as source:
    print("Please wait. I'm working with the mic...")
    # listen for 5 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)
    while not (detectEndWords(context)):
        print("Listening :)")  
        audio = r.record(source, duration=5)
        try:
            context += r.recognize_google(audio) + " "

        except sr.UnknownValueError:
            context += ""
        except sr.RequestError as e:
            context += ""

# Recognize speech using Google (require internet)
try:
    print("I hear you saying:'" + context + "'")

except sr.UnknownValueError:
    print("I missed what you just said...")
except sr.RequestError as e:
    print("Opps, there's something wrong; {0}".format(e))