import setuptools
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ogcmaps",
    version="0.1.0",
    author="52°North",
    author_email="info@52north.org",
    description="Python client and wrapper for OGC Maps API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/52North/api-maps-client",
    project_urls={
        "Bug Tracker": "https://github.com/52North/api-maps-client/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
)
