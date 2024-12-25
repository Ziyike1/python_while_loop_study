message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello {name}!")

prompt = "If you share your name, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello {name}!")

age = input("How old are you? ")
print(age)
print(int(age) + 2)

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou are tall enouth to ride.")
else:
    print("\nYou will be able to ride when you are a little older.")

print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7491412 % 31234)

number = input("Enter a number,and I will tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")