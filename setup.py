from setuptools import setup, find_packages

# Safely read README.md with UTF-8 encoding
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="solo-traveler-cli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer[all]",
    ],
    entry_points={
        "console_scripts": [
            "solo=solo_traveler_cli.main:app",
        ],
    },
    author="Brandon Himpfen",
    author_email="brandon@himpfen.com",
    description="A CLI tool to help solo travelers plan trips, track expenses, pack efficiently, and journal their travels.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/solotravelerorg/solo-traveler-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
