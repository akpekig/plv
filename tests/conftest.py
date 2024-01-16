# pylint: disable=redefined-outer-name
import pytest

from api import routes

@pytest.fixture
def app():
    app = routes.create_app()
    return app


@pytest.fixture
def client(app):
    return app.test_client()
