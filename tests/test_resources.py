import requests

from tests.conftest import get_url


class TestResourcePositive:
    def test_get_list_of_resources(self):
        url = get_url() + 'unknown'
        payload = {}
        headers = {}
        req = requests.get(url, headers=headers, data=payload)
        assert req.status_code == 200

    def test_get_single_resource(self):
        url = get_url() + 'unknown/2'
        payload = {}
        headers = {}
        req = requests.get(url, headers=headers, data=payload)
        assert req.status_code == 200


class TestResourceNegative:
    def test_resource_not_found(self):
        url = get_url() + 'unknown/23'
        payload = {}
        headers = {}
        req = requests.get(url, headers=headers, data=payload)
        assert req.status_code == 404
