#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions

from src.question_a.question_a import get_miles_per_hour
from src.question_b.question_b import get_random_number
from src.question_d.question_d import get_day_of_the_week
from src.question_c.question_c import get_bonus_pay_amount
class Test_Config(unittest.TestCase):
     def test_question_a_config (self):
    
         self.assertEqual(True, Test_Config ())
def test_get_random_number(self):
         self.assertEqual(get_random_number() >= 1, True)
         self.assertEqual(get_random_number() <= 5, True)
 

def test_get_bonus_pay_amount(self):
         self.assertEqual(get_bonus_pay_amount(-1), "Invalid Arguments")
         self.assertEqual(get_bonus_pay_amount(200), 10)
         self.assertEqual(get_bonus_pay_amount(600), 36)
         self.assertEqual(get_bonus_pay_amount(1000), 70)
         self.assertEqual(get_bonus_pay_amount(1500), 120)
         self.assertEqual(get_bonus_pay_amount(2000), "Invalid Arguments")
 


def test_get_day_of_week(self):
         self.assertEqual (get_day_of_the_week(0), 'Invalid number')
         self.assertEqual (get_day_of_the_week(1), 'Monday')
         self.assertEqual (get_day_of_the_week(2), 'Tuesday')
         self.assertEqual (get_day_of_the_week(3), 'Wednesday')
         self.assertEqual (get_day_of_the_week(8), 'Invalid number')
 
def test_get_miles_per_hour(self):
        self.assertEqual (get_miles_per_hour (32,60), 19.883872)
       