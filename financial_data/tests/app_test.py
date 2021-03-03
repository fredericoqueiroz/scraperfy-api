from .fixtures import app, client

def test_app_create(app):
    assert app

#def test_app_healthy(client):
#    with client:
#        response = client.get('/health')
#        assert response.status_code == 200
#        assert response.is_json
#        assert response.json == 'healthy'

