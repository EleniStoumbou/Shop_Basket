class Basket_Two:
    
    def __init__(self):
        self.num_of_each_product = {}

    def add_products(self, product):
        if product not in self.num_of_each_product.keys():
            self.num_of_each_product[product] = 1
        else:
            self.num_of_each_product[product] += 1
        return self.num_of_each_product 



