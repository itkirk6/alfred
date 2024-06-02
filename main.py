import settings
import audio
import database
import stt
import decide

from processText import processText
import commands

def main():
    audioInput = stt.AudioInput()
    
    while(True):
        text = audioInput.getInput()
        d = decide.Decider()
        
        try:
               
            if("alfred" in text):
                        text = settings.stripBeforeSubstring(text,"alfred").replace("alfred","").strip()
                        print(text)
                        processedText = processText(text)
                        output = d.decide(processedText)
                        if output:
                            keyword, args = output

                            command = command.findCommand(keyword)

                            result = command.execute(*args)  #this function parses text as well

                            if result:
                                pass
                                 



                        
                        
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
