## Functions
## function is a named,reusable block of code-you write it once,then"call" whenever you want
# def-means"define a function"-you are creating one
#()- we will use this to pass the information (empty for now)
# colon: below code 

def greet():
    print("Hello ,I am a Robot")

greet()
#write once use many times
def greet(name):
    print(f"Hello,I am{name}")
greet("turtlebot")
greet("Robo")