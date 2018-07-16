import unittest
import json
import pprint
from app import create_app


class BaseTest (unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client

        self.requests = {
            "requests": "This is a request",
            "type": "repair"
        }
    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
