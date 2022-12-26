import requests


def test_get_encoded_url_check_status_code_equals_200():
    """This test checks whether the encoding endpoint returns
     200 status code for a regular request"""
    url = "https://www.finn.auto"
    response = requests.get("http://127.0.0.1:8000/encode/" + url)
    assert response.status_code == 200


def test_get_encoded_url_check_content_type_equals_json():
    """This test checks wheter the encoding endpoint returns a json format"""
    url = "https://www.finn.auto"
    response = requests.get("http://127.0.0.1:8000/encode/" + url)
    assert response.headers["Content-Type"] == "application/json"


def test_get_decoded_url_check_status_code_equals_200():
    """This test checks whether a regular http get request would return status code 200"""
    long_url = "https://www.finn.auto"
    response = requests.get("http://127.0.0.1:8000/encode/" + long_url)
    short_url = response.json()['encoded_url']
    response2 = requests.get("http://127.0.0.1:8000/decode/" + short_url)
    assert response2.status_code == 200


def test_get_decoded_url_check_content_type_equals_json():
    """This test checks whether the decoding endpoint returns a json format"""
    long_url = "https://www.finn.auto"
    response = requests.get("http://127.0.0.1:8000/encode/" + long_url)
    short_url = response.json()['encoded_url']
    response2 = requests.get("http://127.0.0.1:8000/decode/" + short_url)
    assert response2.headers["Content-Type"] == "application/json"


def test_get_decoded_url_check_url_equals_original():
    """This test checks whether when encoding a regular long url to a short one,
     the right url would be returned in decoding the short url"""
    long_url = "https://www.finn.auto"
    response = requests.get("http://127.0.0.1:8000/encode/" + long_url)
    short_url = response.json()['encoded_url']
    response2 = requests.get("http://127.0.0.1:8000/decode/" + short_url)
    response_json = response2.json()
    assert response_json['decoded_url'] == long_url
