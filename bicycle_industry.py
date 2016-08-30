class Bicycle(object):
    def __init__(self, bike_name, weight, production_cost, margin):
        self._bike_name = bike_name
        self._weight = weight
        self._production_cost = production_cost
    @property
    def bike_name(self):
        return self._bike_name
    @bike_name.setter
    def bike_name(self, new_bike_name):
        if isinstance(new_bike_name, str):
            self._bike_name = new_bike_name
        else:
            raise ValueError("Bike name must be a string")
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, new_weight):
        if isinstance(new_weight, int):
            self._weight = new_weight
        else:
            raise ValueError("Weight should be changed to an integer.")
    @property
    def production_cost(self):
        return self._production_cost
    @production_cost.setter
    def production_cost(self, new_production_cost):
        if isinstance(new_production_cost, int):
            self.production_cost = new_production_cost
        else:
            raise ValueError("Production cost must be an integer.")
    def get_marginalized_cost(self, margin):
        return self.production_cost * (1 + margin)



class Bikeshop(object):
    def __init__(self, shop_name, shop_inventory, sell_price, profit):
        self._shop_name = shop_name
        self._shop_inventory = shop_inventory
        self._sell_price = sell_price
        self._profit = profit
    @property
    def shop_name(self):
        return self._shop_name
    @shop_name.setter
    def shop_name(self, new_shop_name):
        if isinstance(new_shop_name, str):
            self._shop_name = new_shop_name
        else:
            raise ValueError("Shop name needs to be a string.")
    @property
    def shop_inventory(self):
        return self._shop_inventory
    @shop_inventory.setter
    def shop_inventory(self, new_shop_inventory):
        if isinstance(new_shop_inventory, dict):
            self._shop_inventory.update(new_shop_inventory)
        else:
            raise KeyError("Shop inventory should be a dictionary.")
    @property
    def sell_price(self):
        return self._sell_price
    @sell_price.setter
    def sell_price(self, new_sell_price):
        if isinstance(new_sell_price, int):
            self._sell_price = new_sell_price
        else:
            raise ValueError("Sell price must be an integer.")
    @property
    def profit(self):
        return self._profit
    @profit.setter
    def profit(self, new_profit):
        if isinstance(new_profit, int):
            self._profit = new_profit
        else:
            raise ValueError("Profit must be an integer.")

class Customers(object):
    def __init__(self, customer_name, funds, buy):
        self._customer_name = customer_name
        self._funds = funds
        self._buy = buy
    @property
    def customer_name(self):
        return self._customer_name
    @customer_name.setter
    def customer_name(self, new_customer_name):
        if isinstance(new_customer_name, str):
            self._customer_name = new_customer_name
        else:
            raise ValueError("Customer name should be a string.")
    @property
    def funds(self):
        return self._funds
    @funds.setter
    def funds(self, new_funds):
        if isinstance(new_funds, int):
            self._funds = new_funds
        else:
            raise ValueError("Funds must be an integer.")
    @property
    def buy(self):
        return self._buy
    @buy.setter
    def buy(self, new_buy):
        if isinstance(new_buy, str):
            self._buy = new_buy
        else:
            ValueError("The buy must be a string")

b1 = Bicycle("Gary Turner Mountain Bike", 45, 145)
b2 = Bicycle("Big Shot Fixed Bike", 25, 125)
b3 = Bicycle("New Trek Racing Bike", 20, 275)
b4 = Bicycle("Odyssey BMX Bike", 40, 250)
b5 = Bicycle("Schwinn Cruiser Bike", 55, 175)
b6 = Bicycle("VoltBike Electric Bike", 85, 400)
bikes = [b1, b2, b3, b4, b5, b6]

customer1 = Customers("Joe", 200, 0)
customer2 = Customers("Michelle", 500, 0)
customer3 = Customers("Taylor", 1000, 0)



##bike = Bicycle("Fasty", 25 , 225)
##print(bike.bike_name)
##print(bike.weight)
##bike.bike_name = "Quick"
##print(bike.bike_name)
##bike.bike_name = "Slow-Slow"
##print(bike.bike_name)


shop1 = Bikeshop("Bikeland", {}, 200, 100)


##print(shop1.shop_name)
##shop1.shop_inventory = {b1.bike_name:20, b2.bike_name:20, b3.bike_name:20, b4.bike_name:20, b5.bike_name:20, b6.bike_name:20}
for bike in bikes:
    print(bike.bike_name)
    shop1.shop_inventory = {bike.bike_name: 20}
print(shop1.shop_inventory)


##print(customer1.customer_name)
##print(customer1.funds)
##print(customer2.customer_name)
##print(customer2.funds)
##print(customer3.customer_name)
##print(customer3.funds)
##shop1.shop_inventory = "cold"
##shop1.shop_name = 0
##bike.bike_name = 8
##bike.weight = "ice"
##bike.production_cost = "fire"
##shop1.sell_price = "Cheese"
##shop1.profit = "cash"
##customer1.funds = "money"
##customer1.customer_name = 7
customer1.buy = 10