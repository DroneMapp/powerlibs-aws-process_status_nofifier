import re
from setuptools import setup

VERSION = '0.2.0'


with open('requirements/production.txt') as requirements_file:
    requires = [item for item in requirements_file]

with open('README.md') as f:
    readme = f.read()


with open('LICENSE') as f:
    package_license = f.read()


setup(
    name='powerlibs-aws-process_status_notifier',
    version=VERSION,
    description="A general helper to notify processes status",
    long_description=readme,
    author='Adolfo W. Sabino',
    author_email='adolfo.w.s@gmail.com',
    url='https://github.com/DroneMapp/powerlibs-aws-process_status_nofifier',
    license=package_license,
    packages=[
        'powerlibs',
        'powerlibs.aws',
        'powerlibs.aws.process_status_notifier'
    ],
    package_data={'': ['LICENSE', 'README.md']},
    include_package_data=True,
    zip_safe=False,
    keywords='generic libraries',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
    install_requires=requires
)
