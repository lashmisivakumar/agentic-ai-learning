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
##Remove an item-remove needsthe actual vaule/name eg:remove("turn")
commands.remove("wait")
print(commands)
##Remove an item from paticular place example from 2nd place-need pop-needs theposition number eg:pop(2)
commands.pop(1)
print(commands)
##The huge agents using the (in)-it decide"do i havethis tool"-it give result true or false(checkingit there  or not)
print("jump"in commands)
print("fly "in commands)
command="jump"
##Now we used (in) in if statement
if command in commands:
    print("Yes,i can")
else:
    print("no,i cant")