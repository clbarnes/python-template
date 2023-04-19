from pathlib import Path

from setuptools import find_packages, setup

with open(Path(__file__).resolve().parent / "README.md") as f:
    readme = f.read()

setup(
    name="{{cookiecutter.package_name}}",
    url="{{cookiecutter.url}}",
    author="{{cookiecutter.author}}",
    description="{{cookiecutter.description}}",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        include=["{{cookiecutter.package_name}}*"]
    ),
    install_requires=[],
    python_requires=">=3.8, <4.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)
