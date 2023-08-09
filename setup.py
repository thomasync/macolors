from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="macolors",
    version="0.0.1",
    author="thomasync",
    author_email="macolors-github@thomascauquil.fr",
    description="Command-line tool for colorizing output of log files and console programs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thomasync/macolors",
    packages=["macolors"],
    license="MIT",
    classifiers=[],
    python_requires=">=3.2",
    install_requires=["colorama"],
    entry_points={
        "console_scripts": ["macolors = macolors.main:main"],
    },
    keywords="color log console terminal logs macos",
    test_suite="tests",
    project_urls={
        "Bug Reports": "https://github.com/thomasync/macolors/issues",
        "Source": "https://github.com/thomasync/macolors",
    },
)
