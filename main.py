import settings
import audio
import database
import stt
import decode

def main():
    audioInput = stt.AudioInput()
    
    while(True):
        text = audioInput.getInput()
        
        try:
               
            if("alfred" in text):
                        text = settings.stripBeforeSubstring(text,"alfred").replace("alfred","").strip()
                        print(text)
                        print(decode.Decode(text).value)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
