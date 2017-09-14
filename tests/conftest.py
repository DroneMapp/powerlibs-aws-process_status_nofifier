import pytest

BASE_ENVIRON = {
    'AWS_ACCESS_KEY_ID': 'test-aws-key-id',
    'AWS_SECRET_ACCESS_KEY': 'shhh...secret',
}


@pytest.fixture
def aws_region_environ():
    return {**BASE_ENVIRON, 'AWS_REGION': 'test-region'}


@pytest.fixture
def aws_region_name_environ():
    return {**BASE_ENVIRON,
            'AWS_REGION_NAME': 'test-region-name',
            'AWS_REGION': 'test-region'}


@pytest.fixture
def no_aws_region_environ():
    return BASE_ENVIRON
