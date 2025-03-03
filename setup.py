from setuptools import setup, find_packages

setup(
    name="fuzzy-controller",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["numpy", "matplotlib"],
    author="Your Name",
    author_email="whizzkid.dpd@gmail.com",
    description="A simple fuzzy logic controller",
    url="https://github.com/prem-dharshan/fuzzy-controller",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
