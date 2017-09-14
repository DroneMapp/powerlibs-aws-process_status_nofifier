import re
from setuptools import setup

VERSION = '0.0.5'


def pip_git_to_setuptools_git(url):
    match = re.match(
        r'git\+https://github.com/(?P<owner>[^/]+)/(?P<repository>[^/]+).git@(?P<tag>.+)',
        url
    )
    if match:
        group_dict = match.groupdict()
        url = "git+https://github.com/{owner}/{repository}.git@{tag}#egg={repository}-{tag}".format(
            **group_dict
        )
        package = '{repository}=={tag}'.format(**group_dict)
    return package, url


def parse_requirements():
    requires = []
    dependency_links = []

    with open('requirements/production.txt') as requirements_file:
        for line in requirements_file:
            if 'git+' in line:
                package, link = pip_git_to_setuptools_git(line.strip())
                dependency_links.append(link)
            else:
                package = line.strip()
            requires.append(package)

    return {'install_requires': requires, 'dependency_links': dependency_links}


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
    packages=['powerlibs', 'powerlibs.aws', 'powerlibs.aws.process_status_notifier'],
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
    **parse_requirements()
)
