class Catalogue_Products:

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price
      
    
        



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

    def __init__(self, products):
        self.products = products
        
      
    def two_plus_one(self, offer_products):
        for product in products.keys():
            if product in offer_products:
                if products[product] > 2:
                    free_products = int(products[product]/3)
                    products[product] - free_products
  

    def discount_offer(self, offer_products, discount):
        for product in products.keys():
            if product in offer_products:
                Catalogue_Products.product_price = -(discount*product


    '''