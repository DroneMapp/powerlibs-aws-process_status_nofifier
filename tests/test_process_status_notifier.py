from powerlibs.aws.process_status_notifier import ProcessStatusNotifier

from unittest import mock

import pytest


@pytest.fixture
def payload():
    return {
        'key': 'value'
    }


@mock.patch('powerlibs.aws.sqs.publisher.SQSPublisher.publish')
def test_success(publish_mock, payload):
    with ProcessStatusNotifier(queue_name='q', process_name='proc-id', payload=payload):
        publish_mock.assert_called_with('q', payload, attributes={'topic': 'proc-id__started'})
    publish_mock.assert_called_with('q', payload, attributes={'topic': 'proc-id__finished'})


@mock.patch('powerlibs.aws.sqs.publisher.SQSPublisher.publish')
def test_multiple_topics(publish_mock, payload):
    with ProcessStatusNotifier(queue_name='q', process_name='proc-id', payload=payload) as notifier:
        notifier.status_topics['finished'].append('custom_topic')
        publish_mock.assert_called_with('q', payload, attributes={'topic': 'proc-id__started'})
    publish_mock.assert_has_calls([
        mock.call('q', payload, attributes={'topic': 'proc-id__finished'}),
        mock.call('q', payload, attributes={'topic': 'custom_topic'})
    ])


@mock.patch('powerlibs.aws.sqs.publisher.SQSPublisher.publish')
def test_custom_topic_name(publish_mock, payload):
    with ProcessStatusNotifier(queue_name='q', process_name='proc-id', payload=payload, topics_format='custom_topics_format__{status}'):
        publish_mock.assert_called_with('q', payload, attributes={'topic': 'custom_topics_format__started'})
    publish_mock.assert_called_with('q', payload, attributes={'topic': 'custom_topics_format__finished'})


@mock.patch('powerlibs.aws.sqs.publisher.SQSPublisher.publish')
def test_failed(publish_mock, payload):
    with pytest.raises(Exception) as exc_info:
        with ProcessStatusNotifier(queue_name='q', process_name='proc-id', payload=payload):
            publish_mock.assert_called_with('q', payload, attributes={'topic': 'proc-id__started'})
            raise Exception('Something wrong is not right.')
        assert exc_info == 'Something wrong is not right'
        publish_mock.assert_called_with('q', {**payload, 'message': 'Something wrong is not right.'}, attributes={'topic': 'proc-id__failed'})
