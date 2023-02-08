"""Setup ecr-lifecycle client"""

# Standard library imports
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).resolve().parent
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='ecr-lifecycle',
    version='0.1.1',
    description='Delete old images tag inside ECR repository',
    long_description=README,
    long_description_content_type="text/markdown",
    python_requires=">=3.6, <4",
    url='https://github.com/austinobioma/python-delete-old-ecrimages.git',
    author='nanih98',
    author_email='test@null.io',
    license='Apache',
    install_requires=['boto3==1.23.1',
                      'botocore==1.26.1', 'jmespath==1.0.0', 'python-dateutil==2.8.2', 's3transfer==0.5.2',
                      'six==1.16.0', 'urllib3==1.26.9'],
    packages=find_packages(include=['ecr_lifecycle']),
    include_package_data=True,
    entry_points={'console_scripts': [
        'ecr-lifecycle=ecr_lifecycle.__main__:main']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
