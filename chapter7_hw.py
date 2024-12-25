#7.1
car = input("Hello, what type of car you seek? ")
print(f"Let me see if I can find you a {car}")


#7.2
perople = input("Hello, How many seat you want to order? ")
perople = int(perople)
if perople > 8:
    print("There are not enough seat.")
else:
    print("Great, wellcome")


#7.3
number = int(input("Please enter a number: "))
if number % 10 == 0:
    print("This number can be divide by 10")
else:
    print("This is not a number I want")


#7.4
active = True
while active:
    toppings = input("\nPlease enter the pizza toppings you want: ")
    if toppings == 'quit':
        active = False
    else:
        print(f"\nWe wll add {toppings} to your pizza.")


#7.5
prmpt = "\nPlease enter your age:"
prmpt += "\nEnter 'quit' to end this program. "
message = ""
while message != 'quit':
    message = input(prmpt)
    if message != 'quit':
        if int(message) < 3:
            print("Fees: 0$")
        elif int(message) < 12:
            print("Fees: 10$")
        else:
            print("Fees: 15$")


#7.6
active = True
while active:
    age = int(input("\nPlease enter your age: "))
    if age < 3:
        print("Fees: 0$")
    elif age < 12:
        print("Fees: 10$")
    else:
        print("Fees: 15$")

    break


#7.7
number_1 = 2
while number_1 > 0:
    print(number_1)


#7.8
sandwich_orders = ['tuna','pastrami','original','beef']
finished_sandwich = []

while sandwich_orders:
    order = sandwich_orders.pop(-1)
    print(f"I made you {order} sandwichs.")
    finished_sandwich.append(order)

for sandwich in finished_sandwich:
    print(sandwich.title())


#7.9
sandwich_orders = ['tuna','pastrami','original','beef','pastrami','pastrami']
finished_sandwich = []
print("Sorry,pastrami are out of our store.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop(-1)
    print(f"I made you {order} sandwichs.")
    finished_sandwich.append(order)

for sandwich in finished_sandwich:
    print(sandwich.title())


#7.10
poll_flag = True
result = {}
while poll_flag:
    check = ['quit','no']
    name = input("\nFirst, What is you name? ")
    if name in check:
        break

    place = input("If you could visit one place in the world, "
                  "where would you go? ")
    if place in check:
        break
    else:
        result[name] = place
        print(f"\nCool {name}, {place} is a nice place. ")
        print("\nWould you like to continue? or type 'quit/no' "
                "to end polling.")
    
    if result:
        for k,v in result.items():
            print(f"\n{k} want to go {v} for travel.")