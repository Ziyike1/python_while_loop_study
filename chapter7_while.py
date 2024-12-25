current_number = 1
while current_number <= 5:
    print(current_number) 
    current_number += 1


prmpt = "\nTell me something, and I wll repeat it back to you:"
prmpt += "\nEnter 'quit' to end this program. "

message = ""
while message != 'quit':
    message = input(prmpt)
    
    if message != 'quit':
        print(message)
    

prmpt = "\nTell me something, and I wll repeat it back to you:"
prmpt += "\nEnter 'quit' to end this program. "

active = True
while active:
    message = input(prmpt)
    
    if message == 'quit':
        active = False
    else:
        print(message)


prmpt = "\nPlease enter the name of city you have visited:"
prmpt += "\n(Enter 'quit' to end this program.) "

while True:
    city = input(prmpt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")


current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Ctrl + C 结束无限循环
x = 1
while x <= 5:
    print(x)
    x += 1