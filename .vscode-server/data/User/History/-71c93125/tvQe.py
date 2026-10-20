## Functions
## function is a named,reusable block of code-you write it once,then"call" whenever you want
# def-means"define a function"-you are creating one
#()- we will use this to pass the information (empty for now)
# colon: below code 

def greet():
    print("Hello ,I am a Robot")

greet()
#write once use many times-nowing passing information
def greet(name):
    print(f"Hello,I am {name}")
greet("turtlebot")
greet("Robo")

def add(a,b):
    return a+b
x=int(input("Enter the value of a"))
y=int(input("Enter the value of b"))
answer=add(x,y)
print(answer)
#-----------------

def battery(level):
    if level<20:
        print("Battery low")
    else:
        print("Battery fine")

battery(15)
battery(60)
#-------------------
def check_battery(level):
    if level<20:
        print("Battery is low")
    else:
        print("Batter is fine")

def robot_status(name,level):
    message=check_battery(level)
    return f"{name} says {message}"
print(robot_status("Turtlebot",15))

