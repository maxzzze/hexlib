from setuptools import setup

setup(
    name="hexlib",
    version="1.81",
    description="Misc utility methods",
    author="simon987",
    author_email="me@simon987.net",
    packages=["hexlib"],
    include_package_data=True,
    package_data={"": [
        "data/*"
    ]},
    install_requires=[
        "influxdb", "siphash", "python-dateutil", "redis", "orjson", "zstandard",
        "u-msgpack-python", "psycopg2-binary", "bs4", "lxml", "nltk", "numpy",
        "matplotlib", "fake-useragent @ git+https://github.com/maxzzze/fake-useragent",
        "requests"
    ]
)
