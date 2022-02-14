MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def show_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def get_coins():
    print("please insert coins.")
    quarters=float(input("How many quarters?: "))
    dimes=float(input("How many dimes?: "))
    nickles=float(input("How many nickles?: "))
    pennies=float(input("How many pennies?: "))
    return(float("{:.2f}".format(0.25*quarters+0.1*dimes+0.05*nickles+0.01*pennies)))

def there_are_resources(flavor):
    if MENU[flavor]["ingredients"]["water"]>resources["water"]:
        print("Sorry there is not enough water")
        return False
    if flavor!="espresso" and MENU[flavor]["ingredients"]["milk"]>resources["milk"]:
        print("Sorry there is not enough milk")
        return False
    if MENU[flavor]["ingredients"]["coffee"]>resources["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    return True

def adjust_resources(flavor):
    resources["money"]+=MENU[flavor]['cost']
    resources["water"]-=MENU[flavor]["ingredients"]["water"]
    resources["milk"]-=MENU[flavor]["ingredients"]["milk"]
    resources["coffee"]-=MENU[flavor]["ingredients"]["coffee"]

def return_change(flavor, amount_inserted):
    if amount_inserted>MENU[flavor]['cost']:
        print(f"Here is ${amount_inserted-MENU[flavor]['cost']} in change.")

def make_cofee(flavor):
    print(f"Here is your {flavor} ☕️. Enjoy!")
    adjust_resources(flavor)


turned_on=True

while turned_on:
    flavor=input("What would you like? (espresso/latte/cappuccino): ")
    if flavor=="off":
        turned_on=False
    elif flavor=='report':
        show_resources()
    elif flavor=="espresso" or flavor=="latte" or flavor=="cappuccino":
        if there_are_resources(flavor):
            amount_inserted=get_coins()
            if amount_inserted>=MENU[flavor]["cost"]:
                return_change(flavor, amount_inserted)
                make_cofee(flavor)
            else:
                print("Sorry, that's not enough money. Money refunded.")