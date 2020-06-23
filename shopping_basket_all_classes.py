'''from Catalogue import exp_catalogue

class Catalogue_Products:
    
    def __init__(self, all_prod):
        self.all_prod = all_prod
'''        

class Basket:
    
    def __init__(self):
        self.num_of_each_product = {}


    def num_of_each(self, basket_products):
        for product in basket_products:
            if product not in self.num_of_each_product.keys():
                self.num_of_each_product[product] = basket_products.count(product)
        return self.num_of_each_product


class Offers:

    def __init__(self, bask_prod, all_prod):
        self.bask_prod =  bask_prod
        self.all_prod = all_prod
        
    
    def two_plus_one(self, plus_offer_prod):
        for product in self.bask_prod.keys():
            if product in plus_offer_prod.keys():
                if self.bask_prod[product] >= plus_offer_prod[product]:
                    self.bask_prod[product] = self.bask_prod[product] - int(self.bask_prod[product]/plus_offer_prod[product])
        return self.bask_prod

    def discount_offer(self, disc_offer_prod):
        for product in self.bask_prod.keys():
            if product in disc_offer_prod.keys():
                self.all_prod[product] = (1 - disc_offer_prod[product]) * self.all_prod[product]
        return self.all_prod    


class Total_Costs:

    def __init__(self, bask_prod, all_prod):
        self.bask_prod =  bask_prod
        self.all_prod = all_prod
      

    def undisc_total(self):
        undisc_total = 0
        for product, num in self.bask_prod.items():
            undisc_total += self.all_prod[product] * num
        return undisc_total


    def disc_total(self, plus_offer_prod, disc_offer_prod, offer_plus, offer_disc):
        disc_total = 0
        for product, num in self.bask_prod.items():
            if product in plus_offer_prod.keys():
                disc_total += self.all_prod[product] * offer_plus[product]
            elif product in disc_offer_prod.keys():
                disc_total += offer_disc[product] * num 
            else:
                disc_total += self.all_prod[product] * num
        return disc_total
    
catalogue = {
            "Baked Beans" : 0.99, 
            "Biscuits" : 1.20, 
            "Sardines" : 1.89, 
            "Shampoo Small" : 2.00,
            "Shampoo Medium" : 2.50, 
            "Shampoo Large" : 3.50
            }

'''catalogue = Catalogue_Products(exp_catalogue)'''


products_i_want_to_buy = ["Biscuits", "Biscuits", "Shampoo Small", "Biscuits", "Biscuits", "Shampoo Small", "Sardines", "Baked Beans"]
plus_offer_prod = {"Biscuits": 3}
disc_offer_prod = {"Shampoo Small": 0.25}

basket = Basket()

offers = Offers(basket.num_of_each(products_i_want_to_buy), catalogue)


total_basket_cost = Total_Costs(basket.num_of_each(products_i_want_to_buy), catalogue)

undiscount_total = total_basket_cost.undisc_total() 

offer_plus = offers.two_plus_one(plus_offer_prod)
offer_disc = offers.discount_offer(disc_offer_prod)
discount_total = total_basket_cost.disc_total(plus_offer_prod, disc_offer_prod, offer_plus, offer_disc)


print(undiscount_total)
print(discount_total)