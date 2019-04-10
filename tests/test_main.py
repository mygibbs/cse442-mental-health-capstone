def test_index(client):
    response = client.get('/index', follow_redirects=True)
    assert response.status_code == 200


def test_achievements(client):
    response = client.get('/achievements', follow_redirects=True)
    assert response.status_code == 200


def test_exercises(client):
    response = client.get('/exercises', follow_redirects=True)
    assert response.status_code == 200


def test_profile(client):
    response = client.get('/profile', follow_redirects=True)
    assert response.status_code == 200
    
def test_activity101(client):
    response = client.get('/activity101', follow_redirects=True)
    assert response.status_code == 200

def test_activity1(client):
    response = client.get('/activity1', follow_redirects=True)
    assert response.status_code == 200

def test_activity2(client):
    response = client.get('/activity2', follow_redirects=True)
    assert response.status_code == 200

def test_activity2_classical(client):
    response = client.get('/activity2_classical', follow_redirects=True)
    assert response.status_code == 200

def test_activity2_stringed(client):
    response = client.get('/activity2_stringed', follow_redirects=True)
    assert response.status_code == 200

def test_activity2_piano(client):
    response = client.get('/activity2_piano', follow_redirects=True)
    assert response.status_code == 200

def test_activity2_wind(client):
    response = client.get('/activity2_wind', follow_redirects=True)
    assert response.status_code == 200

def test_activity2_natural(client):
    response = client.get('/activity2_natural', follow_redirects=True)
    assert response.status_code == 200

def test_activity2_popular(client):
    response = client.get('/activity2_popular', follow_redirects=True)
    assert response.status_code == 200



def test_activity4(client):
    response = client.get('/activity4', follow_redirects=True)
    assert response.status_code == 200

def test_activity5(client):
    response = client.get('/activity5', follow_redirects=True)
    assert response.status_code == 200

def test_activity6(client):
    response = client.get('/activity6', follow_redirects=True)
    assert response.status_code == 200

def test_points(client):
    response = client.get('/update_points', follow_redirects=True)
    assert response.status_code == 200

def test_about(client):
    response = client.get('/about', follow_redirects=True)
    assert response.status_code == 200