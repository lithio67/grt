from setuptools import setup, find_packages

setup(
    name="grt library",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy", "random" # Required for array functionality
    ],
    author="Aidan Liu",
    description="A simplified library with custom function names",
    long_description="This library provides simplified function names: say() for print(), ran() for random(), and arr() for array().",
    long_description_content_type="text/plain",
    url="https://github.com/lithio67/grt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Lichense 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
