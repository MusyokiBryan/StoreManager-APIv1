import unittest
import sys  # fix import errors
from app import create_app
from app.api.V1.models import *
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ConfigTestCase(unittest.TestCase):
    """This class represents the basic configs for all test case"""

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(config="testing")
        self.client = self.app.test_client

        product = Products()
        product.create_product("Bryan", 456)
        product.create_product("Jason", 847)

        sales_s = Sales()
        sales_s.post_a_sale("Brian", 456, 5000)
        sales_s.post_a_sale("jay", 556, 2000)


if __name__ == '__main__':
    unittest.main()
