import pytest
from mead.server import Mead

@pytest.fixture
def mead():
    return Mead()
