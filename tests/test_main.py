import io
import sys
import unittest

from src.main import calculate_bmi, health_check, input_data
from unittest.mock import patch
import math
from io import StringIO

class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start class')

    @classmethod
    def tearDownClass(cls):
        print('end class')

    def setUp(self):
        print('start')

    def tearDown(self):
        print('end')

# @unittest.skipIf()
#     def test_calculate_bmi(self):
#         result = calculate_bmi(1.69,60)
#         self.assertTrue(math.isclose(result,21.0076, rel_tol= 1e-4))
#
#     def test_health_check(self):
#         with patch('sys.stdout',new = io.StringIO()) as fake_output:
#             # health_check(24)
#             health_check(25)
#             # health_check(15)
#             output = fake_output.getvalue().strip()
#             # self.assertEqual(output, '不错，请保持')
#             self.assertEqual(output, '减肥啦')
#             # self.assertEqual(output, '加油吃吧')

    def test_input_data(self,mock_input = (1.70, 60)):
       self.assertEqual(input_data(),mock_input)

if __name__ == '__main__':
    unittest.main()