from setuptools import setup, find_packages

setup(
    name="grt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",  # Required for array functionality
    ],
    author="Aidan Liu",
    description="A simplified library with custom function names",
    long_description="This library provides simplified function names: say() for print(), ran() for random(), and arr() for array().",
    long_description_content_type="text/plain",
    url="https://github.com/yourusername/my_simplified_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
