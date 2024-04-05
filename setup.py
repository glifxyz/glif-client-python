from setuptools import setup, find_packages

setup(
    name="glif_client",
    version="0.1.0",
    author="Raphael Vorias",
    author_email="raphael@glif.app",
    description="A wrapper for the Glif API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "aiohttp>=3.7.4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
