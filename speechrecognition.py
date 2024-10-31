import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something:")
    # Listen to the first phrase and extract it into audio data
    audio = r.listen(source)
    
    try:
        # Recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
