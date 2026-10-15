import requests

def test_json_request_format():
    payload = {
        "title": "test_title",
        "body": "test_body"
    }
    request = requests.Request("POST",
                                "http://example.com",
                                json=payload
                                )
    prepared = request.prepare()
    assert prepared.headers['content-type'] == 'application/json'
    print(prepared.body)


def test_form_request_format():
    payload = {
        "title": "test_title",
        "body": "test_body"
    }
    request = requests.Request("POST",
                               "http://example.com",
                               data = payload
    )

    prepared = request.prepare()
    assert prepared.headers['content-type'] == "application/x-www-form-urlencoded"