import re
from commands import commands
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=key)

class Decider:
    def __init__(self):
        self.commands = commands

    def decide(self, input_string):
        descriptions = [f"index: {x}, {commands[x].description}, {commands[x].returnValue}" for x in range(len(commands))]
        #print(descriptions)
        prompt = f"""
I have a list of command descriptions and their corresponding return values. Here are the descriptions:
keyword: add, Add item to inventory, ['item name']
keyword: remove, Remove item from inventory, ['item name']
keyword: used, Consumed/used some item, ['item name', 'int: amount']
keyword: shop, Going shopping or needs shopping list, []
keyword: receipt, Coming back from a shopping trip or has receipt, []
keyword: out, Ran out of some item, ['item name']

Given the following prompt:
{input_string}

Give me the keyword of the description it most matches, and fill in the return value with the data from the prompt it needs.
This should be in the format: keyword,returnValue
The item name should not include a number, if the amount is not listed that is extraneous information.
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
        print(msg)

        if msg == "False":
            return False
        """
        try:
            #index = int(msg.split(",")[0])

            argument = ",".join([x.strip() for x in msg.split(",")[1:]]).replace("[", "").replace("]", "").replace('"', "")
            args = argument.split(",")

            return args

        except Exception as e:
            print(e)
            print(msg)
            return False"""
        