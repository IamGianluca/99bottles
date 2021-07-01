from setuptools import find_packages, setup  # type: ignore

import bottles

setup(
    name="bottles",
    version=bottles.__version__,
    description="My solution to the exercise in 99 bottles of OOP",
    author="Gianluca Rossi",
    author_email="gr.gianlucarossi@gmail.com",
    license="MIT",
    install_requires=[
        "black>=19.10b0",
        "isort>=5.9.1",
        "mypy>=0.910",
        "pytest>=6.2.0",
    ],
    packages=find_packages("bottles"),
    package_dir={"bottles": "bottles"},
)
