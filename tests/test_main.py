def test_index(client):
    response = client.get('/index', follow_redirects=True)
    assert response.status_code == 200


def test_achievements(client):
    response = client.get('/achievements', follow_redirects=True)
    assert response.status_code == 200


def test_profile(client):
    response = client.get('/profile', follow_redirects=True)
    assert response.status_code == 200
