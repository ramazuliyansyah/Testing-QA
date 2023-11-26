# conftest.py
import pytest
from app import create_app
from .test_models import create_factory

create_factory()

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

@pytest.fixture
def app():
    app = create_app()
    yield app