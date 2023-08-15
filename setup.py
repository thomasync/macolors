from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="macolors",
    version="0.0.5",
    author="thomasync",
    author_email="macolors-github@thomascauquil.fr",
    description="Add colors to terminal command outputs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thomasync/macolors",
    packages=["macolors", "macolors.schemes"],
    package_data={"schemes": ["*.yml", "*.yaml"]},
    include_package_data=True,
    license="MIT",
    classifiers=[],
    python_requires=">=3.6",
    install_requires=["rich", "pyyaml"],
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
