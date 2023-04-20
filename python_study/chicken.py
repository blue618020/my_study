# 한 조건을 가지고 if문을 만드는 여러가지 방법
age = 19
money = 20000
chicken = 50000
beer = 10000
drink = 5000
# if money >= chicken:
#     print("치킨을 먹는다.")
# if money >= beer and age >= 20:
#     print("맥주를 먹는다.")
# if money >= drink:
#     print("음료수를 먹는다.")

# if money >= chicken:
#     print("치킨을 먹는다.")
#     money = money - chicken
# if money >= beer and age >= 20:
#     print("맥주를 먹는다.")
#     money = money - beer
# if money >= drink:
#     print("음료수를 먹는다.")
#     money = money - drink

if money >= chicken:
    print("치킨을 먹는다.")
    if money - chicken >= beer and age >= 20:
        print("맥주를 먹는다.")
        if money - chicken - beer >= drink: 
            print("음료수를 먹는다.")
    if money - chicken >= drink:
         print("음료수를 먹는다.")
elif money >= beer and age >= 20:
    print("맥주를 먹는다.")
    if money - beer >= drink:
        print("음료수를 먹는다.")
elif money >= drink:
    print("음료수를 먹는다.")
