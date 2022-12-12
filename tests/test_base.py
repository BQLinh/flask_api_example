import unittest 

from flask import Flask
from initial.init_database import db


app = Flask(__name__)

class TestBase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db

    def test_login(self):
        print(self.db)
        self.assertEqual(1, 2-1)
