import re
import commands
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

class Decider:
    def __init__(self):
        self.commands = commands.commands

    def decide(self, input_string):
        descriptions = [f"keyword: {key}, {self.commands[key].description}, {self.commands[key].returnValue}\n" for key in commands.commands.keys()]
        #print(descriptions)
        prompt = f"""
I have a list of command descriptions and their corresponding return values. Here are the descriptions:
{"".join(descriptions)}

Given the following prompt:
{input_string}

Give me the keyword of the description it most matches, and fill in the return value with the data from the prompt it needs.
This should be in the format: keyword,returnValue
The item name should not include a number, if the amount is not listed that is extraneous information.
if adding inventory the amount should default to 0 unless otherwise specified.
It the item is given as plural, make it singular.
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
        except Exception as e:
            print(e)
            print("Error calling ChatGPT")
            return False
    
        msg = completion.choices[0].message.content
        print(msg)

        if msg == "False":
            return False
        try:
            #index = int(msg.split(",")[0])
            msg = msg.replace('"','').replace("'", '').replace(" ", '').replace('[','').replace(']','')
            msg = msg.split(',',1)
            msg[1] = msg[1].split(',')
            
            if msg[1] == ['']:
                msg[1] = []
            print(f"return value 1 -> {msg[0]}, return value 2-> {msg[1]}")
            return msg[0], msg[1]

        except Exception as e:
            print(e)
            print(msg)
            return False
        