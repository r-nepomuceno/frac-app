from django.test import Client
def test_health_route():
    c = Client()
    r = c.get("/health/")
    assert r.status_code == 200
    assert b"ok" in r.content
