# 首先，创建一个待验证的用户列表
# 以及一个储存已经验证的用户的列表
unconfirmed_users = ['alice','brain','candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的用户移动到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifing user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# 使用 remove方法以及 while循环删除列表中的重复元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is  your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Polling result ---")
for name, response in responses.items():
    print(f"{name} Would like to climb {response}")
    