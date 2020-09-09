import requests

def test_one():
    r = requests.get("https://api.github.com/events")
    assert r.status_code == 200


def test_two():
    r = requests.get("https://api.github.com/events")
    assert r.encoding == "utf"