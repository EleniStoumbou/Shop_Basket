

class Items:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

   

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
        offer = 0
        for product in self.bask_prod.keys():
            if product in plus_offer_prod.keys():
                if self.bask_prod[product] >= plus_offer_prod[product]:
                    offer += int(self.bask_prod[product]/plus_offer_prod[product]) * self.all_prod[product]
        return offer

    def discount_offer(self, disc_offer_prod):
        offer = 0
        for product in self.bask_prod.keys():
            if product in disc_offer_prod.keys():
                offer += (1 - disc_offer_prod[product]) * self.bask_prod[product] * self.all_prod[product] 
        return offer  

    def grouped_offer(self, group_offer_prod, offer_num):
        group = []
        for product in self.bask_prod.keys():
            if product in group_offer_prod:
                count = self.bask_prod[product] 
                while count > 0:
                    group.append(self.all_prod[product])
                    count -= 1
        group.sort()
        offer = sum(group[:(int(len(group)/offer_num))])
        return offer
            

class Total_Costs:

    def __init__(self, bask_prod, all_prod):
        self.bask_prod =  bask_prod
        self.all_prod = all_prod
      

    def calculate_undiscount_total(self):
        undisc_total = 0
        for product, num in self.bask_prod.items():
            undisc_total += self.all_prod[product] * num
        return round(undisc_total, 2)

    def calculate_discount(self, offers, plus_offer_prod, disc_offer_prod, group_offer_prod, offer_num):
        discount = offers.two_plus_one(plus_offer_prod) + offers.discount_offer(disc_offer_prod) + offers.grouped_offer(group_offer_prod, offer_num)
        return round(discount, 2)

    def calculate_final_total(self, offers, plus_offer_prod, disc_offer_prod, group_offer_prod, offer_num):
        final_total = self.calculate_undiscount_total() -  self.calculate_discount(offers, plus_offer_prod, disc_offer_prod, group_offer_prod, offer_num)
        return round(final_total, 2)

    

    
catalogue = {
            "Baked Beans" : 0.99, 
            "Biscuits" : 1.20, 
            "Sardines" : 1.89, 
            "Shampoo Small" : 2.00,
            "Shampoo Medium" : 2.50, 
            "Shampoo Large" : 3.50
            }