class Catalogue_Products:

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price
    '''    self.catalogue_items = {}
      
    def add_products(self):
        self.catalogue_items[self.product_name] = self.product_price
        '''
class Basket:

    def __init__(self):
        self.num_of_each_product = {}

    def num_of_each(self, basket_products):
        for product in basket_products:
            if product not in self.num_of_each_product.keys():
                self.num_of_each_product[product] = basket_products.count(product)
        return self.num_of_each_product
         



class Special_Offers:

    def __init__(self, products_in_basket, all_products):
        self.products_in_basket = products_in_basket
        self.all_products = all_products
      
    def two_plus_one(self, plus_offer_products):
        
        for product in products_in_basket.keys():
            if product in plus_offer_products:
                if products_in_basket[product] > 2:
                    plus_offer_price += (products_in_basket[product] - int(products_in_basket[product]/3)) * self.all_products[product]
        return offer_price
  

    def discount_offer(self, disc_offer_products, discount):
        for product in products_in_basket.keys():
            if product in disc_offer_products:
                self.all_products[product] = ((1-discount)*self.all_products[product]
        return self.all_products

class Total_Cost:

    def __init__(self,all_products, basket_products):
        self.products_in_basket = products_in_basket
        self.all_products = all_products

    def undiscount_total(self):
        total = 0
        for product,num in basket_products.items():
            total += num * all_products[product]
        return total

    def discount_total(self, ):
        disc_total = 0
        for product,num in basket_products.items():
            if product not in :
                disc_total += num * all_products[product]
            elif product in:
                disc_total += (num * all_products[product]) - offer_
        return total

        


    

    


    