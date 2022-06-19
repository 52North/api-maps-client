import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ogc-maps",
    version="0.0.1",
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
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
