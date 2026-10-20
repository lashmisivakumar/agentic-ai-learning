

def move():
    print("Move called")
def turn():
    print("Turncalled")
def battery():
    print("battery called")


while True:
    r=input("Enter the input: ")
    if r==("quit"): 
        print("Goodbye")
        break
    elif r==("move"):
        move()
    elif r==("turn"):
        turn()
    elif r==("battery"):
        battery()
    else:
        print("Sorry do not know the command")
#---------------------
x=move
print(x)
x()
#----------------------
print("Fucntions Using dictionary label")

while True:
    tools={"move":move,"turn":turn,"battery":battery}
    s=input("Enter the input: ")
    if s==("quit"): 
        print("Goodbye")
        break
    elif s in tools:
        tools[s]() #here it reads the same tools dictionary to see what isallowed to do .it picks a label and your code runs tools[label]()
    else:
        print("Sorry do not know the command")


