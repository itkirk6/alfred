import re
from commands import commands
from openai import OpenAI
client = OpenAI()

class Decider:
    def __init__(self):
        self.commands = commands

    def decide(self, input_string):
        descriptions = [f"index: {x}, {commands[x].description}, {commands[x].returnValue}" for x in range(len(commands))]
        #print(descriptions)
        prompt = f"""
I have a list of command descriptions and their corresponding return values. Here are the descriptions:
{"\n".join(descriptions)}

Given the following prompt:
{input_string}

Give me the index of the description it most matches, and fill in the return value with the data from the prompt it needs.
This should be in the format: index,returnValue
If the prompt does not seem to match any of the descriptions, print False.
Do not print or give me anything other than this explicit format I asked for.
"""
        print(prompt)
        try:
            completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": prompt}
                ]
            )
        except:
            print("ChatGPT Error")
    
        msg = completion.choices[0].message.content

        if msg == "False":
            return False
        
        try:
            index = int(msg.split(",")[0])

            argument = ",".join([x.strip() for x in msg.split(",")[1:]]).replace("[", "").replace("]", "").replace('"', "")
            args = argument.split(",")

            return args

        except:
            print("Unable to parse GPT output")
            return False
        