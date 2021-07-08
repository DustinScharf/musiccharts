from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="musiccharts",
    version="0.0.1",
    description="A small python script to scrap (electronic) music charts into directories with csv files.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/DustinScharf/musiccharts",
    author="DustinScharf",
    author_email="d.scharf.2002@gmail.com",
    keywords="music, charts, dj",
    license="MIT",
    packages=[
        "musiccharts"
    ],
    install_requires=[
        "beautifulsoup4>=4.9.3",
        "certifi>=2021.5.30",
        "chardet>=4.0.0",
        "idna>=2.10",
        "install>=1.3.4",
        "requests>=2.25.1",
        "soupsieve>=2.2.1",
        "urllib3>=1.26.5"
    ],
    include_package_data=True
)
