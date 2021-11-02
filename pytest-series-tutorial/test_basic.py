import pytest

@pytest.mark.login
def test():
    assert 100 == '100', 'integer not equal to string'


