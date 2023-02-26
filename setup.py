import os
from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="prowessive",
    version="0.0.1",
    author="Rubén Pozo Molina",
    author_email="rubenpozomolina@gmail.com",
    description="RAD for pwa",
    license="MIT",
    keywords="RAD pwa",
    url="https://github.com/RubenPozoMolina/prowessive",
    install_requires=['Flask', 'gunicorn'],
    extras_require={
        'dev': [
            'pytest',
            'selenium',
            'pyyaml',
            'waiting',
            'requests'
        ]
    },
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
