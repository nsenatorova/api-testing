import json

import requests

from tests.conftest import get_url


class TestUserPositive:
    def test_get_list_of_users(self):
        url = get_url() + 'users?page=2'
        payload = {}
        headers = {}
        req = requests.get(url, headers=headers, data=payload)
        assert req.status_code == 200

    def test_get_single_user(self):
        url = get_url() + 'users/2'
        payload = {}
        headers = {}
        req = requests.get(url, headers=headers, data=payload)
        assert req.status_code == 200

    def test_create_user(self):
        url = get_url() + 'users'
        payload = json.dumps({
            "name": "morpheus",
            "job": "leader"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        req = requests.post(url, headers=headers, data=payload)
        assert req.status_code == 201

    def test_update_user(self):
        url = get_url() + 'users/2'
        payload = json.dumps({
            "name": "morpheus",
            "job": "zion resident"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        req = requests.patch(url, headers=headers, data=payload)
        assert req.status_code == 200

    def test_register_successful(self):
        url = get_url() + 'register'
        payload = json.dumps({
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        req = requests.post(url, headers=headers, data=payload)
        assert req.status_code == 200

    def test_login_successful(self):
        url = get_url() + 'login'
        payload = json.dumps({
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        req = requests.post(url, headers=headers, data=payload)
        assert req.status_code == 200

    def test_delete_user(self):
        url = get_url() + 'users/2'
        payload = {}
        headers = {}
        req = requests.delete(url, headers=headers, data=payload)
        assert req.status_code == 204


class TestUserNegative:
    def test_single_user_not_found(self):
        url = get_url() + 'users/23'
        payload = {}
        headers = {}
        req = requests.get(url, headers=headers, data=payload)
        assert req.status_code == 404

    def test_register_unsuccessful(self):
        url = get_url() + 'register'
        payload = json.dumps({
            "email": "sydney@fife"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        req = requests.post(url, headers=headers, data=payload)
        assert req.status_code == 400

    def test_login_unsuccessful(self):
        url = get_url() + 'login'
        payload = json.dumps({
            "email": "peter@klaven"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        req = requests.post(url, headers=headers, data=payload)
        assert req.status_code == 400
