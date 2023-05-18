"""
BaseTest

This class should be the parent class to each system test.
It gives each test a Flask test client that we can use.
"""

from unittest import TestCase
from app import app


class BaseTest(TestCase):
    # runs before each test
    def setUp(self):
        # for the lifetime of this app we are in testing mode
        app.testing = True
        self.app = app.test_client
