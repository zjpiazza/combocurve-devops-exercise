from flask.testing import FlaskClient

def test_request_count_increments(test_client: FlaskClient):
  response_1 = test_client.get("/")  
  response_2 = test_client.get("/")
  assert response_2.json["invocation_count"] > response_1.json["invocation_count"]