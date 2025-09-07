import unittest
from my_calculator import my_adder

class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        self.assertEqual(my_adder(5,3),8)
    
    def test_negative_with_negative(self):
        self.assertEqual(my_adder(5,3),2) 

#不是直接執行此程式，使用終端機來操作
#輸入 python -m unittest