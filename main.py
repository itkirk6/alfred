import settings
import audio
import database
import stt
import decide

from processText import processText
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
                        processedText = processText(text)
                        output = d.decide(processedText)
                        print(0)
                        if output:
                            print("1")
                            keyword, args = output
                            print(2)
                            command = commands.commands[keyword]
                            print(3)
                            result = command.execute(*args)
                            print(4)
                            print(result)
                            print(5)
                                 



                        
                        
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
