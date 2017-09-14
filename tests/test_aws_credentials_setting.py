from unittest import mock

import pytest

from powerlibs.aws.process_status_notifier import ProcessStatusNotifier


# Tests for the AWS_REGION / AWS_REGION_NAME environ setting

def test_with_region_default_environ(default_region_environ):
    with mock.patch.dict('os.environ', default_region_environ, clear=True):
        notifier = ProcessStatusNotifier(queue_name='test_queue_name', process_name='test_process_name')
        assert notifier.notifier.aws_region == 'test-region-default-environ'


def test_with_region_alternative_environ(alternative_region_environ):
    with mock.patch.dict('os.environ', alternative_region_environ, clear=True):
        notifier = ProcessStatusNotifier(queue_name='test_queue_name', process_name='test_process_name')
        assert notifier.notifier.aws_region == 'test-region-alternative-environ'


def test_without_region_environ(no_region_environ):  # pylint: disable=unused-argument
    with mock.patch.dict('os.environ', {}, clear=True):
        with pytest.raises(KeyError):
            notifier = ProcessStatusNotifier(queue_name='test_queue_name', process_name='test_process_name')
            assert notifier.notifier.aws_region == ''

# Tests for the AWS_ACCESS_KEY_ID / AWS_KEY_ID environ setting


def test_with_access_key_id_default_environ(default_access_key_id_environ):
    with mock.patch.dict('os.environ', default_access_key_id_environ, clear=True):
        notifier = ProcessStatusNotifier(queue_name='test_queue_name', process_name='test_process_name')
        assert notifier.notifier.aws_access_key_id == 'test-access-key-id-default-environ'


def test_with_access_key_id_alternative_environ(alternative_access_key_id_environ):
    with mock.patch.dict('os.environ', alternative_access_key_id_environ, clear=True):
        notifier = ProcessStatusNotifier(queue_name='test_queue_name', process_name='test_process_name')
        assert notifier.notifier.aws_access_key_id == 'test-access-key-id-alternative-environ'


def test_without_access_key_id(no_access_key_id_environ):  # pylint: disable=unused-argument
    with mock.patch.dict('os.environ', {}, clear=True):
        with pytest.raises(KeyError):
            notifier = ProcessStatusNotifier(queue_name='test_queue_name', process_name='test_process_name')
            assert notifier.notifier.aws_access_key_id == ''

# Tests for the AWS_SECRET_ACCESS_KEY / AWS_SECRET_KEY


def test_with_secret_access_key_default_environ(default_secret_access_key_environ):
    with mock.patch.dict('os.environ', default_secret_access_key_environ, clear=True):
        notifier = ProcessStatusNotifier(queue_name='test_queue_name', process_name='test_process_name')
        assert notifier.notifier.aws_secret_access_key == 'test-secret-access-key-default-environ'


def test_with_secret_access_key_alternative_environ(alternative_secret_access_key_environ):
    with mock.patch.dict('os.environ', alternative_secret_access_key_environ, clear=True):
        notifier = ProcessStatusNotifier(queue_name='test_queue_name', process_name='test_process_name')
        assert notifier.notifier.aws_secret_access_key == 'test-secret-access-key-alternative-environ'


def test_without_secret_access_key(no_secret_access_key_environ):  # pylint: disable=unused-argument
    with mock.patch.dict('os.environ', {}, clear=True):
        with pytest.raises(KeyError):
            notifier = ProcessStatusNotifier(queue_name='test_queue_name', process_name='test_process_name')
            assert notifier.notifier.aws_secret_access_key == ''
