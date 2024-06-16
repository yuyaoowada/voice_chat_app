import speech_recognition as sr


def recognize_speech():
    """Speech recognition"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        res = r.recognize_google(audio, language="ja-JP")
        print(f"　　私　　:{res}")
        return res
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
