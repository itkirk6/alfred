#speechrecognition,LINUX python3-pyaudio, WINDOWS pyaudio,pyttsx3,
import speech_recognition as sr
import tts
import decode


class AudioInput():
    # Initialize the recognizer 
    def __init__(self):
        self.r = sr.Recognizer() 
        pass
    def inputLoop(self):

        # Loop infinitely for user to speak
        while(1):    
            
            # Exception handling to handle exceptions at the runtime
            try:
                
                # use the microphone as source for input.
                with sr.Microphone() as source:
                    
                    # wait for a second to let the recognizer adjust the energy threshold based on
                    # the surrounding noise level 
                    self.r.adjust_for_ambient_noise(source, duration=0.2)
                    
                    #listens for the user's input 
                    audio = self.r.listen(source)
                    
                    # Using google to recognize audio
                    MyText = self.r.recognize_google(audio)
                    MyText = MyText.lower()
                    
                    print(f"AUDIO INPUT -> {MyText}")
                    
                    if("alfred" in MyText.split()[0]):
                        MyText = MyText.replace("alfred","").strip()
                        print(MyText)
                        print(decode.Decode(MyText).value)
                    
                    #tts.textToSpeech(MyText)
                    
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                
            except sr.UnknownValueError:
                print("unknown error occurred")\

AIP = AudioInput()
AIP.inputLoop()
    

