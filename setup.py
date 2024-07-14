# setup.py

from setuptools import setup, find_packages

setup(
    name="icnc",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv",
    ],
    entry_points={
        'console_scripts': [
            'icnc=cli._cli:main',
        ],
    },
)
