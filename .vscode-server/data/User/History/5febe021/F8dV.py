commands=["move","turn","stop"]
print(commands)
print(commands[0])
print(commands[1])
print(commands[2])
for i in commands:
    print(i)
##commands list printfrom 0 to 1 here 2 not take in forloop ittake only first 2 addres only 
for i in range(2):
    print(commands[i])
commands.append("wait")
print(commands)
## counting the list
print (len(commands))
##change an item
commands[0]="jump"
print(commands)