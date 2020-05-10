class Machine:

    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9

    def buy(self, choice):
        success_phrase = "I have enough resources, making you a coffee!"
        no_water = "Sorry, not enough water!"
        no_milk = "Sorry, not enough milk!"
        no_beans = "Sorry, not enough coffee beans!"
        no_cups = "Sorry, not enough coffee cups!"
        if self.cups == 0:
            print(no_cups)
        if choice == "1":  # espresso
            if self.water >= 250 and self.beans >= 16:
                self.coffee_make(choice)
                print(success_phrase)
            else:
                print(no_water if self.water < 250 else no_beans)
        elif choice == "2":  # latte
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20:
                self.coffee_make(choice)
                print(success_phrase)
            else:
                if self.water < 350:
                    print(no_water)
                else:
                    print(no_milk if self.milk < 75 else no_beans)
        elif choice == "3":  # cappuccino
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12:
                self.coffee_make(choice)
                print(success_phrase)
            else:
                if self.water < 200:
                    print(no_water)
                else:
                    print(no_milk if self.milk < 100 else no_beans)
        elif choice == "back":
            return None

    def coffee_make(self, choice):
        self.cups -= 1
        if choice == "1":
            self.money += 4
            self.water -= 250
            self.beans -= 16
        elif choice == "2":
            self.money += 7
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
        elif choice == "3":
            self.money += 6
            self.water -= 200
            self.milk -= 100
            self.beans -= 12

    def fill(self, water, milk, beans, cups):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def take(self):
        self.money = 0

    def __str__(self):
        return """The coffee machine has:
        {} of water
        {} of milk
        {} of coffee beans
        {} of disposable cups
        ${} of money""".format(self.water, self.milk, self.beans, self.cups, self.money)


coffee_machine = Machine()

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input("> ")
    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_machine.buy(input("> "))
    elif action == "fill":
        print("Write how many ml of water do you want to add:")
        add_water = int(input("> "))
        print("Write how many ml of milk do you want to add:")
        add_milk = int(input("> "))
        print("Write how many grams of coffee beans do you want to add:")
        add_coffee_beans = int(input("> "))
        print("Write how many disposable cups of coffee do you want to add:")
        add_cups = int(input("> "))
        coffee_machine.fill(add_water, add_milk, add_coffee_beans, add_cups)
    elif action == "take":
        print("I gave you ${}".format(coffee_machine.money))
        coffee_machine.take()
    elif action == "remaining":
        print(coffee_machine)
    elif action == "exit":
        break
