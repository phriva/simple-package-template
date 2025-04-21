from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="helloworld",
    version="0.0.1",
    author="Peter",
    author_email="riva.pedrohenrique@gmail.com",
    description="This is a basic Hello World",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="github.com/phriva/"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
