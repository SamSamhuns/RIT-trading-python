import unittest
from ritpytrading  import trader

class TestTraderMethods(unittest.TestCase):
    def setUp(self):
        self._sample_trader_resp = {
          "trader_id": "string",
          "first_name": "string",
          "last_name": "string",
          "nlv": 0
        }

    def test_trader(self):
        method_obj = trader.trader_response_handle(self._sample_trader_resp)
        class_obj = self._sample_trader_resp
        self.assertEqual(method_obj, class_obj)


if __name__ == "__main__":
    unittest.main()
