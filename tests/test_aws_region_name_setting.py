from unittest import mock

import pytest

from powerlibs.aws.process_status_notifier import ProcessStatusNotifier


def test_with_aws_region(aws_region_environ):
    with mock.patch.dict('os.environ', aws_region_environ, clear=True):
        notifier = ProcessStatusNotifier(queue_name='test_queue_name', process_name='test_process_name')
        assert notifier.notifier.aws_region == 'test-region'


def test_with_aws_region_name(aws_region_name_environ):
    with mock.patch.dict('os.environ', aws_region_name_environ, clear=True):
        notifier = ProcessStatusNotifier(queue_name='test_queue_name', process_name='test_process_name')
        assert notifier.notifier.aws_region == 'test-region-name'


def test_without_aws_region_at_all(no_aws_region_environ):
    with mock.patch.dict('os.environ', {}, clear=True):
        with pytest.raises(KeyError):
            notifier = ProcessStatusNotifier(queue_name='test_queue_name', process_name='test_process_name')
            assert notifier.notifier.aws_region == ''
