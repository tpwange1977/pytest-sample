import requests
import src.simple as app

# custom class to be the mock return value
# will override the requests.Response returned from requests.get
class MockResponse:
    status_code = 200
    text = "OK"
    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}



def test_get_json(monkeypatch):

    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # app.get_json, which contains requests.get, uses the monkeypatch
    result = app.hello("")
    assert result.status_code == 200