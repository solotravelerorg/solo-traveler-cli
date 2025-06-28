from setuptools import setup, find_packages

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
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to help solo travelers plan trips, track expenses, pack efficiently, and journal their travels.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/solo-traveler-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)