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
#--------------------------------------------

def add(a,b):
    return a+b
x=int(input("Enter the value of a"))
y=int(input("Enter the value of b"))
answer=add(x,y)
print(answer)
#--------------------------------------------

def battery(level):
    if level<20:
        print("Battery low")
    else:
        print("Battery fine")

battery(15)
battery(60)
#-------------------------------------------
def check_battery(level):
    if level<20:
        return "Battery is low"
    else:
        return "Batter is fine"

def robot_status(name,level):
    message=check_battery(level)
    return f"{name} says {message}"
a=int(input("Enter the battery value"))
print(robot_status("Turtlebot",a))

#-----------------------------
# Storing fucntions without running them(dictionary used here)

def hello():
    print("Hello Lashmi")
def bye():
    print("Bye lashmi")
a=hello
print(a)
a()
greetings={"hi":hello,"bye":bye}
print("bye" in greetings)# output is true(bye exists) only not the value
greetings["bye"]()# here we are fetch the function by its label
#greeting["bye"]----eg:TV--take the bye remote out of the box
#() press the button (tv)


#no pointer in python instead it uses reference eg:bye ,hello this all refrence the memory where the value is living

#-----------------------------------------------------------------

# Try/except-handling errors gracefully.

# try/except is for when might crash and you can't check beforehand
# Agents lean(big jump) on try/expect a lot because APIs and AI replies fail in messy
# In unpredictable ways you can't check in advance
#-----------------------------------------------------

# if/else and try/except both are cousins both about choosing path.
#  for example: age=int("hello")---for this code there's no simple (if)
            #if/else-"i will check and act safely"
            #try/except-"act and recover if it goes wrong"
#  here hello is not number so it crash at that time, we cant test properly with if condition its unpredictable
# try:--"attempt the risky code" 
# try works skip except
# except:--if anything wrong in try ,do this instead  crashing the program do calmly what gave

try:
    age=int(input("Enter the age"))
    print("your age is",age)

except:
    print("That was not valid number")#it catch the error instead of crashin

#--------------------------------------------------------------------
# Error:-builtin names in python not keyword
# ValueError-the value wrong kind,like int("hello")
# TypeError - mixing things that don't go together like, "cat"+5
# ZeroDivisionError-dividing by ZeroDivisionError
# KeyError-asking a dictionary for a label thatdoesn't exist
#Exception-anything else unexcepted or went wrong

robot={"battery":50,"speed":10}

try:
    age=int(input("Enter the age: "))
    answer=10/age
    print("Result is:",answer)
    robot["color"]
    print(robot)
    total="cat"+5
except ValueError:
    print("That was not valid number")
except TypeError:
    print("you cannot mix number and text")
except ZeroDivisionError:
    print("you cant divide by zero")
except KeyError:
    print("label does not exist")
except Exception:
    print("something unexcepted went wrong")
#--------------------------------------------------------------------
try:
    age=int(input("Enter the age: "))
    print("The age is:",age)
except ValueError as e:
    print("Something went wrong:",e)#e chosen name, for error which caught e-give actual error message

#------------------------------------------------------------------------