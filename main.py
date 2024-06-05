import settings
import audio
import database
import stt
import decide
import tts

import processText
import commands

def main():
    audioInput = stt.AudioInput()
    d = decide.Decider()
    
    while(True):
        print("Listening now")
        text = audioInput.getInput()
        
        
        try:
               
            if("alfred" in text):
                        text = settings.stripBeforeSubstring(text,"alfred").replace("alfred","").strip()
                        print(text)
                        processedText = processText.processText(text)
                        output = d.decide(processedText)
                        if output:
                            keyword, args = output
                            command = commands.commands[keyword]
                            result = command.execute(*args)
                            print(result)

                            tts.textToSpeech(result)

                                 



                        
                        
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
