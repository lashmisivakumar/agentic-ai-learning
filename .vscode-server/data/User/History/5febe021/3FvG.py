commands=["move","turn","stop"]
print(commands)
print(commands[0])
print(commands[1])
print(commands[2])
for i in commands:
    print(i)
for i in range(2):
    print(commands[i])
commands.append("wait")
print(commands)
print (len(commands))