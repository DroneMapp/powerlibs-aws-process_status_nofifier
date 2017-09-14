import pytest

BASE_ENVIRON = {
    'AWS_ACCESS_KEY_ID': 'test-access-key-id-default-environ',
    'AWS_SECRET_ACCESS_KEY': 'test-secret-access-key-default-environ',
    'AWS_REGION': 'test-region-default-environ',
}

# REGION


@pytest.fixture
def default_region_environ():
    return BASE_ENVIRON


@pytest.fixture
def alternative_region_environ():
    return {**BASE_ENVIRON, 'REGION': 'test-region-alternative-environ'}


@pytest.fixture
def no_region_environ():
    return {k: v for k, v in BASE_ENVIRON.items() if k != "AWS_REGION"}

# ACCESS_KEY_ID


@pytest.fixture
def default_access_key_id_environ():
    return BASE_ENVIRON


@pytest.fixture
def alternative_access_key_id_environ():
    return {**BASE_ENVIRON, 'ACCESS_KEY_ID': 'test-access-key-id-alternative-environ'}


@pytest.fixture
def no_access_key_id_environ():
    return {k: v for k, v in BASE_ENVIRON.items() if k != "AWS_ACCESS_KEY_ID"}


# SECRET_ACCESS_KEY


@pytest.fixture
def default_secret_access_key_environ():
    return BASE_ENVIRON


@pytest.fixture
def alternative_secret_access_key_environ():
    return {**BASE_ENVIRON, 'SECRET_ACCESS_KEY': 'test-secret-access-key-alternative-environ'}


@pytest.fixture
def no_secret_access_key_environ():
    return {k: v for k, v in BASE_ENVIRON.items() if k != 'AWS_SECRET_ACCESS_KEY'}
