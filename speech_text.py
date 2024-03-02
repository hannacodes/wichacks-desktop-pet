# pip install SpeechRecognition
# pip install PyAudio

import speech_recognition as sr
import tasks

recognizer = sr.Recognizer()

def capture_voice_input(): 
    with sr.Microphone() as source: 
        print("Listening...")
        audio = recognizer.listen(source)
    return audio 

def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text

def process_voice(text):
    words = text.lower().split(" ")
    if "goodbye" in text.lower():
        print("Goodbye")
        return True
    elif words[0] == "google":
        tasks.open_google(text[7:])
    else:
        print("huh")
    return False

def voice_command():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice(text)

if __name__ == '__main__':
    voice_command()

