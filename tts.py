import pyttsx3

# Function to convert text to speech
def textToSpeech(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

