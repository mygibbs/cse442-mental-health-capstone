def not_found_error(client):
    response = client.get('/404.html', follow_redirects=True)
    assert response.status_code == 404

    response = client.get('/not_a_web_page.html', follow_redirects=True)
    assert response.status_code == 404


def internal_error(client):
    response = client.get('/500.html', follow_redirects=True)
    assert response.status_code == 500
