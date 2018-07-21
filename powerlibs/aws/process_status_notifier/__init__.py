import os
import traceback

from cached_property import cached_property

from powerlibs.aws.sqs.publisher import SQSPublisher  # pylint: disable=no-name-in-module, import-error

# flake8: noqa E501 pylint: disable=line-too-long


class ProcessStatusNotifier:

    def __init__(self, queue_name, process_name, topics_format='{process_name}__{status}', payload=None, extra_queues=None):
        self.process_name = process_name
        self.payload = payload if payload else dict()
        self.queue_name = queue_name
        self.extra_queues = extra_queues or list()
        self._load_basic_topics(topics_format)

        self.is_final = self.payload.get('is_final', False)

    @cached_property
    def notifier(self):
        return SQSPublisher(**get_aws_credentials_from_env())

    def _load_basic_topics(self, topics_format):
        stati = 'started', 'finished', 'failed'
        self.status_topics = {
            status: [topics_format.format(
                process_name=self.process_name,
                status=status
            )] for status in stati
        }

    def __repr__(self):
        return '<Process Status Notifier for {}>'.format(self.process_name)

    def __enter__(self, *args):
        self.notify('started')
        return self

    def __exit__(self, exc_type, exc_value, trc_back):
        if exc_type is None:
            return self.notify('finished')

        payload = dict(self.payload)
        payload['message'] = str(exc_value)
        payload['traceback'] = ''.join(traceback.format_tb(trc_back))

        self.notify('failed', payload=payload)
        raise exc_type(exc_value)

    def notify(self, status, payload=None):
        topics = self.status_topics[status]
        payload = payload if payload else self.payload

        if status == 'started':
            payload['is_final'] = False
        else:
            payload['is_final'] = self.is_final

        for topic in topics:
            self.notifier.publish(self.queue_name, payload, attributes={'topic': topic})
            for queue in self.extra_queues:
                self.notifier.publish(queue, payload, attributes={'topic': topic})


def get_aws_credentials_from_env():
    return {
        'aws_secret_access_key': os.environ.get('SECRET_ACCESS_KEY') or os.environ.get('AWS_SECRET_ACCESS_KEY'),
        'aws_access_key_id': os.environ.get('ACCESS_KEY_ID') or os.environ.get('AWS_SECRET_KEY_ID'),
        'aws_region': os.environ.get('REGION') or os.environ.get('AWS_REGION'),
    }
