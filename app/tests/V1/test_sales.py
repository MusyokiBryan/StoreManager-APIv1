import unittest
from app.tests.V1.base import ConfigTestCase
import json


class SalesTest(ConfigTestCase):
    """this class contains Product tests"""

    def test_see_sales(self):
        response = self.client().get("/api/v1/sales")
        self.assertEqual(response.status_code, 200)

    def test_get_a_sale(self):
        response = self.client().get("/api/v1/sale/1")
        self.assertEqual(response.status_code, 200)

    def test_post_a_sale(self):
        sale = {"product_name": "shirts", "number": 5500, "sell_price": 500}
        response = self.client().post("/api/v1/sales", data=json.dumps(sale), content_type="application/json")
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
