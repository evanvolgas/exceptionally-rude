from random import randint

rudemsg = list()
with open ('messages.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        rudemsg.append(line)

x = len(rudemsg) - 1
y = randint(0,x)

print x
print y
print rudemsg[y]


#now to  write a function that overrides regular error messages and can be pip installed, etc.
