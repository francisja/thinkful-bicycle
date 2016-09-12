import random

class Bicycle(object):
    def __init__(self, bike_name, weight, production_cost):
        self._bike_name = bike_name
        self._weight = weight
        self._production_cost = production_cost
    @property
    def bike_name(self):
        """
        returns the bike name with the @property decorator
        """
        return self._bike_name
    @bike_name.setter
    def bike_name(self, new_bike_name):
        """
        sets the new bike name with the @setter decorator as long as the new bike name is a string
        """
        if isinstance(new_bike_name, str):
            self._bike_name = new_bike_name
        else:
            raise ValueError("Bike name must be a string")
    @property
    def weight(self):
        """
        returns the weight of the bike with the @property decorator
        """
        return self._weight
    @weight.setter
    def weight(self, new_weight):
        """
        sets the new weight with the @setter decorator as long as the new weight is an integer
        """
        if isinstance(new_weight, int):
            self._weight = new_weight
        else:
            raise ValueError("Weight should be changed to an integer.")
    @property
    def production_cost(self):
        """
        returns the production cost of the bike with the @property decorator
        """
        return self._production_cost
    @production_cost.setter
    def production_cost(self, new_production_cost):
        """
        sets the new production cost with the @setter decorator as long as the new cost is an integer
        """
        if isinstance(new_production_cost, int):
            self.production_cost = new_production_cost
        else:
            raise ValueError("Production cost must be an integer.")
    def get_marginalized_cost(self, margin):
        """
        takes the production cost and multiplies it by 1 + the marginal increase of the store
        """
        return self.production_cost * (1 + margin)

class Bikeshop(object):
    def __init__(self, shop_name, shop_inventory, margin, sell_price, profit):
        self._shop_name = shop_name
        self._shop_inventory = shop_inventory
        self._margin = margin
        self._sell_price = sell_price
        self._profit = profit
    @property
    def shop_name(self):
        """
        returns shop name with the @property decorator
        """
        return self._shop_name
    @shop_name.setter
    def shop_name(self, new_shop_name):
        """
        sets the new shop name with the @setter decorator as long as the new name is a string
        """
        if isinstance(new_shop_name, str):
            self._shop_name = new_shop_name
        else:
            raise ValueError("Shop name needs to be a string.")
    @property
    def shop_inventory(self):
        """
        returns shop inventory with the @property decorator
        """
        return self._shop_inventory
    @shop_inventory.setter
    def shop_inventory(self, new_shop_inventory):
        """
        sets the new shop inventory with the @setter decorator as long as the new inventory is a dictionary
        """
        if isinstance(new_shop_inventory, dict):
            self._shop_inventory.update(new_shop_inventory)
        else:
            raise KeyError("Shop inventory should be a dictionary.")
    @property
    def margin(self):
        """
        returns the margin with the @property decorator
        """
        return self._margin
    @margin.setter
    def margin(self, new_margin):
        """
        sets the new margin with the @setter decorator as long as the new margin is an integer
        """
        if isinstance(new_margin, int):
            self._margin = new_margin
        else:
            raise ValueError("Margin needs to be an integer.")
    @property
    def sell_price(self):
        """
        returns the selling price with the @property decorator by creating a dictionary of the bike name with the marginalized cost of the bike
        """
        prices = {}
        for bike in bikes:
            selling_price = {bike.bike_name: bike.get_marginalized_cost(self.margin)}
            prices.update(selling_price)
        return prices
    @property
    def profit(self):
        return self._profit
    def sell_bike(self, new_bicycle):
        if isinstance(new_bicycle, Bicycle):
            new_bike_name = new_bicycle.bike_name
            cost = self.sell_price[new_bike_name]
            pcost = new_bicycle.production_cost
            self._profit = cost - pcost
        else:
            raise ValueError("The new bike needs to be from the Bicycle class")




class Customers(object):
    def __init__(self, customer_name, funds, bicycle):
        self._customer_name = customer_name
        self._funds = funds
        self._bicycle = bicycle
    @property
    def customer_name(self):
        """
        returns the customer name with the @property decorator
        """
        return self._customer_name
    @customer_name.setter
    def customer_name(self, new_customer_name):
        """
        sets the new customer name with the @setter decorator as long new name is a string
        """
        if isinstance(new_customer_name, str):
            self._customer_name = new_customer_name
        else:
            raise ValueError("Customer name should be a string.")
    @property
    def funds(self):
        """
        returns the customer's funds with the @property decorator
        """
        return self._funds
    @funds.setter
    def funds(self, new_funds):
        """
        sets the new customer's funds with the @setter decorator as long new name is an integer
        """
        if isinstance(new_funds, int):
            self._funds = new_funds
        else:
            raise ValueError("Funds must be an integer.")
    @property
    def bicycle(self):
        return self._bicycle
    def buy_bicycle(self, new_bicycle, bike_shop):
        if isinstance(new_bicycle, Bicycle) and isinstance(bike_shop, Bikeshop):
            self._bicycle = new_bicycle
            new_bike_name = new_bicycle.bike_name
            cost = bike_shop.sell_price[new_bike_name]
            self._funds = self._funds - cost
        else:
            raise ValueError("New bike needs to be a bike in the Bicycle class.")
    def get_affordable_bikes(self, shops):
        """
        returns a list of affordable bikes for the customer by comparing their funds with the selling price of the shop with the @property decorator
        """
        affordable_bikes = []
        for shop in shops:
            for model, price in shop.sell_price.items():
                if self.funds >= price:
                    affordable_bikes.append(model)
        return affordable_bikes


b1 = Bicycle("Gary Turner Mountain Bike", 45, 145)
b2 = Bicycle("Big Shot Fixed Bike", 25, 125)
b3 = Bicycle("New Trek Racing Bike", 20, 475)
b4 = Bicycle("Odyssey BMX Bike", 40, 250)
b5 = Bicycle("Schwinn Cruiser Bike", 55, 375)
b6 = Bicycle("VoltBike Electric Bike", 85, 700)
bikes = [b1, b2, b3, b4, b5, b6]

c1 = Customers("Joe", 200, None)
c2 = Customers("Michelle", 500, None)
c3 = Customers("Taylor", 1000, None)
customer_list = [c1, c2, c3]

s1 = Bikeshop("Bikeland", bikes, 0.2, {}, 0)
my_shops = [s1]

for customer in customer_list:
    print(customer.get_affordable_bikes(my_shops))
c1.buy_bicycle(b1, s1)
print(c1.bicycle.bike_name)
print(c1.funds)
s1.sell_bike(b1)
print(s1.profit)
##for bike in bikes:
##    print(bike.production_cost)
##for customer in customer_list:
##    print( "With {0}'s budget of ${1}, the bikes that can be purchased are the {2}.".format(customer.customer_name, customer.funds, customer.get_affordable_bikes))
##for bike in bikes:
##    s1.shop_inventory[bike.bike_name] = 20
##print(s1.shop_inventory)
##profit_earned = 0
##for customer in customer_list:
##    bike_bought = random.choice(customer.get_affordable_bikes)
##    new_balance = customer.funds - s1.sell_price[bike_bought]
##    print("{0} has purchased the {1}. It was sold for ${2}. That leaves {3} with ${4} left in the bicycle fund.".format(customer.customer_name, bike_bought, s1.sell_price[bike_bought], customer.customer_name, new_balance))
##    s1.shop_inventory[bike_bought] -= 1
##print(s1.shop_inventory)
##print(s1.sell_price)

