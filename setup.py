from setuptools import setup, find_packages

setup(
    name='icnc', 
    version='1.0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'icnc = icnc.main:main'  
        ]
    },
    install_requires=[
        'python-dotenv',
        'openai==0.12.6'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
