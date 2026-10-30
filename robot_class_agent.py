import os                           #Here we are using as that is our operatingsystem as os builtin
from google import genai
from dotenv import load_dotenv           #Anotherone method to call paticular tool from that package dotenv 


load_dotenv()                                       # We are calling dotenv-open your.env file and loads whats inside 
api_key=os.getenv("GEMINI_API_KEY")                 # Fetches the key by its label and stores it in a variable called api_key #gemini_api_key is case sensitive must in caos as in the file .env
client=genai.Client(api_key=api_key)                # make yourconnections,hands your key to the toolbox so that open the door

class Robot:
    def __init__(self,name,battery_level):
        self.name=name
        self.battery_level=battery_level
    def status(self):
        print(f"Value of Robot is {self.name} is {self.battery_level}")
    def charge(self):
        print(f"New battery level is {self.battery_level+10}%")
    def move(self):
        print("Move called")
    def turn(self):
        print("Turncalled")
    def battery(self):
        print("battery called")
        print(f"Battery level is {self.battery_level} %")
    def stop(self):
        print("Robot stopped")

r1=Robot("turtle",50)

tools={"move":r1.move,"turn":r1.turn,"battery":r1.battery,"stop":r1.stop}
while True:
    request=input("Enter your request: ")
    if request=="quit":
        break
    else:
        prompt=f"you are robot,tools:move,turn,battery,stop.Reply with only the tool name that fits this request {request}"# here what are the function you want tocall you must mention that in prompt so that it will work
        try:
            response=client.models.generate_content(model="gemini-flash-latest",contents=prompt) 

            choice=response.text.strip()
            print("AI chose: ",choice)

            if choice in tools:
                tools[choice]()
            else:
                print("sorry,i dont have a tool for that")

        except Exception: #here we are finding error so we are using exception istead of bare except
            print("Sorry your AI is busy")