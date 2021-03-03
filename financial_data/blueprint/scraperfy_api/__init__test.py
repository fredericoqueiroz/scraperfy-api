from financial_data.tests.fixtures import app, client

def test_api_healthy(client):
    with client:
        response = client.get('/api/v1/scraperfy/')
        assert response.status_code == 200
