print(".")
print(".")
print(".")
print(".")


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
}

#COINS

quarter = .25
dime = .10
nickle = .05
penny = .01

num_quarters = 0
num_dimes = 0
num_nickles = 0
num_pennies = 0

quarter_amount = num_quarters*.25
dime_amount = num_dimes*.10
nickle_amount = num_nickles*.05
penny_amount = num_pennies*.01
amount_paid = quarter_amount + dime_amount + nickle_amount + penny_amount 

resources_okay = True
machine_on = True

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']

e_water = MENU["espresso"]["ingredients"]["water"]
e_coffee = MENU["espresso"]["ingredients"]["coffee"]
e_cost = MENU["espresso"]["cost"]

l_water = MENU["latte"]["ingredients"]["water"]
l_coffee = MENU["latte"]["ingredients"]["coffee"]
l_milk = MENU["latte"]["ingredients"]["milk"]
l_cost = MENU["latte"]["cost"]

c_water = MENU["cappuccino"]["ingredients"]["water"]
c_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
c_milk = MENU["cappuccino"]["ingredients"]["milk"]
c_cost = MENU["cappuccino"]["cost"]

def report():
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")

def coins(cost):
    num_quarters = int(input("how many quarters?"))
    num_dimes = int(input("how many dimes?"))
    num_nickles = int(input("how many nickles?"))
    num_pennies = int(input("how many pennies?"))
    quarter_amount = num_quarters*.25
    dime_amount = num_dimes*.10
    nickle_amount = num_nickles*.05
    penny_amount = num_pennies*.01

    amount_paid = round(quarter_amount + dime_amount + nickle_amount + penny_amount, 2)
    if amount_paid < cost:
        print("Sorry, more coins needed")
    elif amount_paid >= cost:
        change = round(amount_paid - cost, 2)
        print(f"Your change is {change}")

while resources_okay == True and machine_on == True:
    amount_paid = quarter_amount + dime_amount + nickle_amount + penny_amount 
    order = input("What would you like to order? ('e' espresso/'l' latte/'c' cappuccino): ")

    if order == "report":
        print (f"Water: {water} ml")
        print (f"Milk: {milk}ml")
        print (f"Coffee: {coffee}g")
    elif order == "off":
        machine_on = False
        print ("Machine shutting down!")
    elif order == "e":
        if e_water >= water:
            resources_okay = False
            print("Sorry, there is not enough water in the machine")
        elif e_coffee >= coffee:
            resources_okay = False
            print("Sorry, there is not enough coffee in the machine")
        else:
            coins(e_cost)
            water -= e_water
            coffee -= e_coffee
            report()
            print ("Enjoy your espresso")
    elif order == "c":
        if c_water >= water:
            resources_okay = False
            print("Sorry, there is not enough water in the machine")
        elif c_coffee >= coffee:
            resources_okay = False
            print("Sorry, there is not enough coffee in the machine")
        elif c_milk >= milk:
            resources_okay = False
            print("Sorry, there is not enough milk in the machine")
        else:
            coins(c_cost)
            milk -= c_milk
            water -= c_water
            coffee -= c_coffee
            report()
            print ("Enjoy your cappuccino")
    elif order == "l":
        if l_water >= water:
            resources_okay = False
            print("Sorry, there is not enough water in the machine")
        elif l_coffee >= coffee:
            resources_okay = False
            print("Sorry, there is not enough coffee in the machine")
        elif l_milk >= milk:
            resources_okay = False
            print("Sorry, there is not enough milk in the machine")
        else:
            coins(l_cost)
            milk -= l_milk
            water -= l_water
            coffee -= l_coffee
            report()
            print ("Enjoy your latte")



#TODO: Option to turn off coffee machine


print(".")
print(".")
print(".")
print(".")