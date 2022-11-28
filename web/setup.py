import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="fuzzcoin",
    version="0.1.1",
    url="http://fuzzcoin.kr/",
    license="MIT",
    maintainer="SSLab Georgia Tech",
    maintainer_email="aaskar@gatech.edu",
    description="The web interface for fuzzcoin.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "Flask-Security-Too",
        "wheel",
        "bcrypt",
        "jsonschema",
        "Flask-WTF",
        "flask_caching",
    ],
    extras_require={"test": ["pytest", "coverage", "black"]},
)
