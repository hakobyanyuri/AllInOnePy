class Human:
    # Class attributes for default name and age
    default_name = "No name"
    default_age = 0
    
    def __init__(self, name=default_name, age=default_age):
        # Instance attributes for name, age, money, and home
        self.name = name
        self.age = age
        self.__money = 0
        self.__home = None

    def info(self):
        # Method to return information about the human
        return f"Name: {self.name}, Age: {self.age}, Money: {self.__money}, Home: {self.__home}"

    @staticmethod
    def default_info():
        # Static method to return default information
        return f"Default Name: {Human.default_name}, Default Age: {Human.default_age}"

    def __make_deal(self, house, price):
        # Private method to handle the house purchase deal
        self.__money -= price
        self.__home = house

    def earn_money(self, amount):
        # Method to increase the money of the human
        self.__money += amount

    def buy_house(self, house, discount):
        # Method to buy a house with a given discount
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
            print("House purchased successfully!")
        else:
            print("Not enough money to buy the house.")

class House:
    def __init__(self, area, price):
        # Instance attributes for area and price of the house
        self._area = area
        self._price = price

    def final_price(self, discount):
        # Method to calculate the final price after discount
        return self._price * (1 - discount)

class SmallHouse(House):
    def __init__(self, price):
        # Initialize a small house with a fixed area of 40
        super().__init__(40, price)

# Tests
print(Human.default_info())  # Print default human information

human = Human("John", 30)  # Create a human instance
print(human.info())  # Print human information

small_house = SmallHouse(100000)  # Create a small house instance
human.buy_house(small_house, 0.1)  # Attempt to buy the house with a 10% discount

human.earn_money(90000)  # Human earns more money
print(human.info())  # Print updated human information

human.buy_house(small_house, 0.1)  # Attempt to buy the house again with a 10% discount
print(human.info())  # Print final human information



