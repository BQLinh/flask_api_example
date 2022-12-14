import unittest 

from flask import Flask
from initial.init_database import db
import json
from app import app

class TestBase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db
        # self.client = self.app.test_client()

        # create user
        payload = json.dumps({
            "name": "linh",
            "email": "linh@gmail.com",
            "password": "1234"
        })
        self.app.post('/register', headers={"Content-Type": "application/json"}, data=payload)

    def test_login_fail(self):
        # Given
        payload = json.dumps({
            "email": "paurakh011@gmail.com",
            "password": "mycoolpassword"
        })

        # When
        response = self.app.post('/login', headers={"Content-Type": "application/json"}, data=payload)
        data = response.get_json()
        # Then
        self.assertEqual(data['result'], "This user is not exit")
        self.assertEqual(400, response.status_code)

    def test_login_pass(self):
        # Given
        payload = json.dumps({
            "name": "linh",
            "email": "linh@gmail.com",
            "password": "1234"
        })
        # When
        response = self.app.post('/login', headers={"Content-Type": "application/json"}, data=payload)

        data = response.get_json()
        print(data)

        # Then
        self.assertEqual(200, response.status_code)

    def tearDown(self) -> None:
        # with self.app.app_context():
        #     self.db.drop_all()
        return super().tearDown()

# if __name__ == '__main__':
#     unittest.main()