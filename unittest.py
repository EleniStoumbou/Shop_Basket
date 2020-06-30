import unittest
from shopping_basket_all_classes import Basket, Offers, Total_Costs

class TestBasket(unittest.TestCase):
    '''Tests for Basket'''

    def test_num_of_each(self):
        basket = Basket()
        my_basket = ["Biscuits", "Biscuits", "Shampoo Small", "Biscuits"]
        basket.num_of_each(my_basket)

        self.assertEqual(basket.num_of_each_product, {"Biscuits" : 3, "Shampoo Small" : 1})

unittest.main()

class TestOffers(unittest.TestCase):
    pass
    


class TestTotal_Costs(unittest.TestCase):
    pass

        