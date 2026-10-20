import os                           #Here we are using as that is our operatingsystem as os builtin
from google import genai
from dotenv import load_dotenv           #Anotherone method to call paticular tool from that package dotenv 


load_dotenv()                                       # We are calling dotenv-open your.env file and loads whats inside 
api_key=os.getenv("GEMINI_API_KEY")                 # Fetches the key by its label and stores it in a variable called api_key #gemini_api_key is case sensitive must in caos as in the file .env
client=genai.Client(api_key=api_key)                # make yourconnections,hands your key to the toolbox so that open the door



def move():
    print("Move called")
def turn():
    print("Turncalled")
def battery():
    print("battery called")

tools={"move":move,"turn":turn,"battery":battery}

request=input("Enter your request: ")
prompt=f"you are robot,tools:move,turn,battery.Reply with only the tool name that fits this request {request}"
response=client.models.generate_content(model="gemini-flash-latest",contents=prompt) 

choice=response.text.strip()
print("AI chose: ",choice)

if choice in tools:
    tools[choice]()
else:
    print("sorry,i dont have a tool for that")