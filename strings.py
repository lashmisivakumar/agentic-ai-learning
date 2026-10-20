##Formated string-(f-String) little f before the quotes
name="lashmi"
print(f"Hello {name}")

##can do calculations andmaths(all 4 operation(+,-,*./,(%-remainder only it give)  ) inside the curly bracket
battery=75
print(f"battery value is {battery} percent")
print(f"In five minutes it will drop to {battery-10}")
print(f"modulo of two number{17%2}")
#--------------------------------------------------
robot="turtle"
action="moving"
speed="90"
print(f"{robot} is {action} with battery {speed} percent")
print(str(robot)+" is "+str(action)+" with battery "+str(speed)+" percent")


##Join two strings together
first="lashmi"
last="sivakumar"
full=first+" "+last
print(full)

#Change to capitals or small letters
word="hello"
print(word.upper())
print(word.lower())

#.strip() remove or cleans the spaces before and after the word
word="  hello  "
print("[" + word + "]")
print("hi"+ word + "good")
print("[" + word.strip() +  "]")

#length of  text-(len)-it works on text(strings) and list not on plain number ,works on multiple peices "it count the space too"
word="hello word"  
print(len(word)) ##o/p=10 -count space too

#picking out part of a word by position
print(word[0])
print(word[1])
##--------------------

#Slicing down
#printing the letters using  position
print(word[0:3])
print(word[1:4])#here it will print from the possition 1 to 3 (but not include 4th position)
