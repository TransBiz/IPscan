from setuptools import setup, find_packages

setup(
    name='scan_ip',
    version='0.0.1dev0',
    author='Yvictor',
    author_email='fate2314@gmail.com',
    packages=find_packages(),
    install_requires=["requests",
                      "beautifulsoup4",
                      "html5lib",
                      "raven"],
)