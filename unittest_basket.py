import unittest
from shopping_basket_all_classes import Basket, Offers, Total_Costs
from catalogue import build_catalogue

class TestBasket(unittest.TestCase):
    '''Tests for Basket'''

    def test_num_of_each(self):
        basket = Basket()
        my_basket = ["Biscuits", "Biscuits", "Shampoo Small", "Biscuits"]
        basket.num_of_each(my_basket)

        self.assertEqual(basket.num_of_each_product, {"Biscuits" : 3, "Shampoo Small" : 1})

class TestOffers(unittest.TestCase):

    def setUp(self):
        self.basket = Basket()
        self.catalogue = build_catalogue()

    def test_four_biscuits(self):

        offers = Offers(self.basket.num_of_each(["Biscuits", "Biscuits", "Biscuits", "Biscuits"]), self.catalogue)
        discount = offers.two_plus_one({"Biscuits" : 3, "Shampoo Small" : 2})
        self.assertEqual(discount, 1.20)
    
    def test_biscuits_baked_beans(self):
    
        offers = Offers(self.basket.num_of_each(["Biscuits", "Biscuits", "Baked Beans","Baked Beans","Baked Beans", "Baked Beans", "Biscuits"]), self.catalogue)
        discount = offers.two_plus_one({"Biscuits" : 3, "Baked Beans" : 4})
        self.assertEqual(discount, 2.19)

    def test_discount_biscuits_shampoo_small(self):
        offers = Offers(self.basket.num_of_each(["Biscuits", "Shampoo Small",  "Biscuits", "Shampoo Large" , "Sardines", "Baked Beans"]), self.catalogue)
        discount = offers.discount_offer({"Biscuits" : 0.5,  "Shampoo Small": 0.25})
        self.assertEqual(discount, 1.70)
    
    def test_grouped_offer(self):
        offers = Offers(self.basket.num_of_each(["Shampoo Small", "Shampoo Large", "Shampoo Large", "Shampoo Large" ,"Shampoo Medium", "Shampoo Medium", "Baked Beans"]), self.catalogue)
        discount = offers.grouped_offer(["Shampoo Small", "Shampoo Medium", "Shampoo Large"], 3)
        self.assertEqual(discount, 4.50)

class TestTotal_Costs(unittest.TestCase):

    def setUp(self):
        self.basket = Basket()
        self.catalogue = build_catalogue()
        self.my_basket = ["Biscuits", "Biscuits", "Shampoo Small", "Biscuits", "Biscuits", "Shampoo Small", "Shampoo Large" , "Sardines", "Baked Beans"]
        self.plus_offer_prod = {"Biscuits": 3}
        self.disc_offer_prod = {"Baked Beans": 0.25}
        self.group_offer_prod = ["Shampoo Small", "Shampoo Medium", "Shampoo Large"]
        self.offer_num = 3
        self.offers = Offers(self.basket.num_of_each(self.my_basket), self.catalogue)
        self.cost = Total_Costs(self.basket.num_of_each(self.my_basket), self.catalogue)

    def test_calculate_undiscount_total(self):

        undiscount_total = self.cost.calculate_undiscount_total() 
        discount = self.cost.calculate_discount(self.offers, self.plus_offer_prod, self.disc_offer_prod, self.group_offer_prod, self.offer_num) 
        discount_total = self.cost.calculate_final_total(self.offers, self.plus_offer_prod, self.disc_offer_prod, self.group_offer_prod, self.offer_num)
        self.assertEqual(undiscount_total, 15.18)
        self.assertEqual(discount, 3.45)
        self.assertEqual(discount_total, 11.73)

unittest.main()