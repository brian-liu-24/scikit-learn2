import pytest

import sklearn1


@pytest.fixture
def print_changed_only_false():
    sklearn1.set_config(print_changed_only=False)
    yield
    sklearn1.set_config(print_changed_only=True)  # reset to default
