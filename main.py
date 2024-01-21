from coffe_menu import MENU
from coffe_menu import resources


def customer_serving():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice in MENU:
        return user_choice
    else:
        print("Please choose one of the following drinks available:")


def report():
    resources_left = resources
    print(
        f"Water: {resources_left['water']}ml\nMilk: {resources_left['milk']}ml\nCoffee: {resources_left['coffee']}g\nMoney: ${resources_left['money']:.2f}"
    )


def check_resource(drink):
    if "ingredients" in MENU[drink]:
        required_resources = MENU[drink]["ingredients"]
        for resource, amount in required_resources.items():
            if resources[resource] < amount:
                print(f"Sorry, there isn't enough {resource}.")
                return False
        return True
    else:
        print(f"Invalid drink: {drink}")
        return False


def process_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total_amount


def coffe_machine_operations():
    power_on = True

    def turn_off():
        nonlocal power_on
        print("Coffee machine is now off")
        power_on = False
        exit()

    while power_on:
        user_input = input(
            "What would you like? (espresso/latte/cappuccino/report/off): "
        ).lower()

        if user_input == "off":
            turn_off()
        elif user_input == "report":
            report()
        elif user_input in MENU:
            order = user_input
            if check_resource(order):
                print(f"Making {order}")
                total_amount = process_coins()
                cost_of_drink = MENU[order]["cost"]

                if total_amount < cost_of_drink:
                    print("Sorry, that's not enough money. Money refunded.")
                else:
                    change = total_amount - cost_of_drink
                    print(f"Transaction successful! Here is your {order}.")
                    if change > 0:
                        print(f"Here is ${change:.2f} dollars in change.")
                    resources["money"] += cost_of_drink

                    for resource, amount in MENU[order]["ingredients"].items():
                        resources[resource] -= amount

                    print("Report after purchasing:")
                    report()
                    print(f"Here is your {order}. Enjoy!")
        else:
            print("Please enter a valid option.")


coffe_machine_operations()