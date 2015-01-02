# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 09:53:40 2012

@author: JJung
"""

#
# homogeneous buyers
#
class homogeneous_buyer:
    # initialize the buyer
    def __init__ (self):
        self.shift = 0

    # define demand quantity as a function of price
    def quantity(self, price):
        return max(c + self.shift- d * price, 0)

    # introduce a demand shock
    def shock (self, shock):
        self.shift = shock

#
# price-taking seller
#
class walrasian_seller:
    # initialize inventory to zero
    def __init__(self):
        self.inventory = 0

    # define supply quantity as a function of price
    def quantity(self, price):
        return max(a + b * price, 0)

    # this seller offers the Walrasian price
    def price(self):
        return walras.price()

    # produce goods
    def produce(self):
        quantity = self.quantity(self.price())
        if self.inventory < quantity:
            self.inventory += (quantity - self.inventory)

    # sell goods
    def sell(self, quantity):
        self.inventory -= quantity


##
## learning seller
##
#class learning_seller:
#    # initialize inventory to zero and clear sales history
#    def __init__(self):
#        self.inventory = 0
#        self.prevsales = 0
#        self.sales = 0
#
#    # define supply quantity as a function of price
#    def quantity(self, price):
#        return max(a + b * price, 0)
#
#    # offer the Walrasian price initially and then use history
#    def price(self):
#        return self.nextprice
#
#    # produce goods
#    def produce(self):
#        if self.sales > 0 and self.prevsales > 0:
#            self.nextprice *= (1.0 + (self.sales-self.prevsales) /
#            self.prevsales)
#        elif self.sales == 0 and self.prevsales > 0:
#            self.nextprice *= 0.5
#        else:
#            self.nextprice = walras.price()
#            quantity = self.quantity(self.nextprice)
#        if self.inventory < quantity:
#            self.inventory += (quantity - self.inventory)
#            self.prevsales = self.sales
#            self.sales = 0
#
#    # sell goods
#    def sell(self, quantity):
#        self.inventory -= quantity
#        self.sales += quantity

#
# define the Walrasian auctioneer
#
class auctioneer:

    # calculate the Walrasian equilibrium price
    def calculate(self, buyers, sellers):
        # begin with price zero and change it incrementally
        price = 0.0
        increment = 100.0
        # see whether the equilibrium price is positive or negative
        supply = sum (map (lambda s: s.quantity (price), sellers))
        demand = sum (map (lambda b: b.quantity (price), buyers))
        positive = (supply < demand)
        # discover the equilibrium price
        while abs (supply - demand) > 0.0000001:
            if supply < demand:
                price += increment
                if not positive:
                    increment /= 2
            else:
                price -= increment
                if positive:
                    increment /= 2
            supply = sum (map (lambda s: s.quantity (price), sellers))
            demand = sum (map (lambda b: b.quantity (price), buyers))
        # save the equilibrium price for later
        self.equilibrium = price

	# return the Walrasian equilibrium price
	def price(self):
		return self.equilibrium


#
# define the basic model
#
def model(buyer_factory, seller_factory):
    # we haven’t seen any results yet
    results = []
    # create the buyers and sellers
    buyers = [buyer_factory() for b in range (B)]
    sellers = [seller_factory() for s in range (S)]
    # for each period...
    for period in range(P):
        # introduce a demand shock
        if period == int(P / 4):
            for b in buyers:
                b.shock(demand_shock)

        # allow the auctioneer to determine the equilibrium price
        walras.calculate(buyers, sellers)
        # engage in production
        for s in sellers:
            s.produce()

        # initialize running totals
        units = 0
        sales = 0

	    # for each buyer...
        for b in buyers:

            # identify the seller offering the best deal
            quantity = 0

            for s in sellers:
                if min(b.quantity(s.price()), s.inventory) > quantity:
                    quantity = min(b.quantity(s.price()), s.inventory)
                    seller = s

            # buy from this seller
            if quantity:
                seller.sell(quantity)
                units += quantity
                sales += quantity * seller.price()

        # determine end-of-period inventory
        inventory = sum(map(lambda s: s.inventory, sellers))

        # save this period’s results
        results.append ((period, units, sales, inventory))

    # return the results to the caller
    return results


#
# run a model
#
def run(name, model):
    # execute the model multiple times
    results = [model() for i in range (I)]
    # initialize totals
    units = [0 for p in range (P)]
    sales = [0 for p in range (P)]
    inventory = [0 for p in range (P)]

    # calculate totals
    for r in results:
        for (p,u,s,i) in r:
            units[p] += u
            sales[p] += s
            inventory[p] += i

	# calculate averages
	for p in range(P):
	    units[p] /= I
	    sales[p] /= I
	    inventory[p] /= I

	# create the results file
	file = open(name + ".csv", "w")

	# write the header
	file.write("Period,Volume,AvgPrice,Inventory\n")

	# write results
	for p in range (P):
	    file.write("%d,%f,%f,%f \n" %(p, units[p], sales[p]/units[p], inventory[p]))

    # close the output file
    file.close()


# -----------------------------------------------------------------------------
#
# define number of buyers, sellers, periods, and iterations
#
B = 1000
S =50
P = 200
I =10
#
# consider Qs = a + bP, Qd=c-dP... give some
# concrete values for a, b, c, and d
#
a = 100
b =10
c =20
d =7

#
# define a demand shock (a change to the value of c)
#
demand_shock = -3

#
# create a Walrasian auctioneer
#
walras = auctioneer()

#
# invoke the models
#
run ("classical",
     lambda: model(lambda: homogeneous_buyer(),lambda: walrasian_seller()))

#run("learning",
#lambda: model(
#    lambda: homogeneous_buyer(),
#    lambda: learning_seller()))

# end of supply-demand.py