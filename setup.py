from setuptools import setup, find_packages


with open("README.rst") as readme_file
    readme=readme_file.read()

setup(
    name="matrixloader",
    version="0.0.1",
    description="a library for reading matrices and graphs for various libraries",
    long_description=readme,
    license="BSD2"
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries"
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    keywords='matrix graph',
    packages=find_packages(exclude=['test']),
    install_requires=[],
    extras_require={
        'numpy' : ['numpy, scipy'],
        'networkx': ['networkx'],
    }
)
