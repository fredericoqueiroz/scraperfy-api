from financial_data.tests.fixtures import app, client
from . import URL_PREFIX

def test_api_healthy(client):
    with client:
        response = client.get(URL_PREFIX)
        assert response.status_code == 200
