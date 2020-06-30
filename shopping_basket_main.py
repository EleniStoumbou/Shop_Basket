from shopping_basket_all_classes import Basket, Offers, Total_Costs, Items
from catalogue import build_catalogue

catalogue = build_catalogue()


my_basket = ["Biscuits", "Biscuits", "Shampoo Small", "Biscuits", "Biscuits", "Shampoo Small", "Shampoo Large" , "Sardines", "Baked Beans"]
plus_offer_prod = {"Biscuits": 3}
disc_offer_prod = {"Baked Beans": 0.25}
group_offer_prod = ["Shampoo Small", "Shampoo Medium", "Shampoo Large"]
offer_num = 3


basket = Basket()

offers = Offers(basket.num_of_each(my_basket), catalogue)


cost = Total_Costs(basket.num_of_each(my_basket), catalogue)

undiscount_total = cost.calculate_undiscount_total() 

discount = cost.calculate_discount(offers, plus_offer_prod, disc_offer_prod, group_offer_prod, offer_num)
discount_total = cost.calculate_final_total(offers, plus_offer_prod, disc_offer_prod, group_offer_prod, offer_num)


print(undiscount_total)
print(discount)
print(discount_total)
