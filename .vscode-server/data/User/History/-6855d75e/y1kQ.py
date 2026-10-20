##List-list-uses [] square brackets and dictionary uses curly bracket{}
##list have second job too depending where u use them  also pick item by position:command[0],or letter word[0]
##Dictionary have second job too depending where u use them  also appear in f-string-formatted string:print(f"Hello {name}")
## Making a list[]-item in order found by position
## Makingng a dictionary{}-pairs found by label


## A dictionary always has those "label:value" pairs with colons
robot={"battery":75,"speed":10}
print(robot)
##guesing the value by label
print(robot["battery"])
#change the value
robot["battery"]=60
print(robot)
#add another one label and value to the dictionary
robot["name"]="turtlebot"
print(robot)
## "key" is the exact word of label (key is like "i")checking
for key in robot:
    print(key,robot[key])
##in 
print("battery" in robot)
print("color" in robot)