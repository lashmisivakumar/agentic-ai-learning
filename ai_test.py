# import google.generativeai as genai -----------#Everytime we need to call package for that we give nickname as genai -----it outdated said by ubuntu so going to gen ai

import os                           #Here we are using as that is our operatingsystem as os builtin
from google import genai
from dotenv import load_dotenv           #Anotherone method to call paticular tool from that package dotenv 


load_dotenv()                                       # We are calling dotenv-open your.env file and loads whats inside 
api_key=os.getenv("GEMINI_API_KEY")                 # Fetches the key by its label and stores it in a variable called api_key #gemini_api_key is case sensitive must in caos as in the file .env
client=genai.Client(api_key=api_key)                # make yourconnections,hands your key to the toolbox so that open the door
print(api_key)

response=client.models.generate_content(model="gemini-flash-latest",contents="say hello to me in one line")    #picks which ai brain needto use gemini-flash-latest free user freindlyand fast and send your question through the door to thr ai
print(response.text)                                            # pulls the reply out and show it
