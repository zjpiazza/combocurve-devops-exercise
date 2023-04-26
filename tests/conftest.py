import pytest
from hello_world import app


@pytest.fixture()
def test_client():
  return app.test_client()