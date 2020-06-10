from shopping_basket_functions import  Catalogue_Products, Basket
from basket_class_alternatives import Basket_Two

catalogue = Catalogue_Products("spagetti", 1.22)
print(catalogue.product_name)

my_basket = Basket()
print(my_basket.num_of_each(["spaggeti", "spaggeti", "chips"]))

my_basket_two = Basket_Two()
print(my_basket_two.add_products("spaggeti"))
print(my_basket_two.add_products("spaggeti"))
print(my_basket_two.add_products("chips"))
