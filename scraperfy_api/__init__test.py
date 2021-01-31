from scraperfy_api.test.fixtures import app, client

def test_app_create(app):
    assert app

def test_app_healthy(client):
    with client:
        resp = client.get('/health')
        assert resp.status_code == 200
        assert resp.is_json
        assert resp.json == 'healthy'