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
         

'''

class Special_Offers:

    #products =  lista me proionta sto kalathi (num_of_each_product)

    def __init__(self, products_in_basket):
        self.products_in_basket = products_in_basket
        
      
    def two_plus_one(self, offer_products):
        
        for product in products_in_basket.keys():
            if product in offer_products:
                if products_in_basket[product] > 2:
                    offer_price = (products_in_basket[product] - int(products_in_basket[product]/3)) * self.product_price
  

    def discount_offer(self, offer_products, discount):
        for product in products_in_basket.keys():
            if product in offer_products:
                self.product_price[product] = ((1-discount)*self.product_price[product])

    

    '''


    