from setuptools import find_packages, setup

setup(
    name="code",
    version="1.0.0",
    author="Himel Das",
    author_email="60639301+thehimel@users.noreply.github.com",
    description="A repository to store code snippets.",
    long_description="Various code snippets are stored in this repository.",
    url="https://github.com/thehimel/code",
    packages=find_packages(),
    install_requires=[
        "black>=23.9.1",
        "isort>=3.11.1",
        "flake8>=6.1.0",
        "requests>=2.31.0",
        "pytest>=7.4.2",
        "pytest-mock>=3.11.1",
        "boto3>=1.28.62",  # aws_s3
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
