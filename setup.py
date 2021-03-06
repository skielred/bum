"""bum - setup.py"""
from setuptools import setup, find_packages

try:
    import bum
except (ImportError, SyntaxError):
    print("error: bum requires Python 3.6 or greater.")
    quit(1)


try:
    import pypandoc
    LONG_DESC = pypandoc.convert("README.md", "rst")
except(IOError, ImportError, RuntimeError):
    LONG_DESC = open('README.md').read()


VERSION = bum.__version__
DOWNLOAD = "https://github.com/skielred/bum/archive/%s.tar.gz" % VERSION


setup(
    name="bum",
    version=VERSION,
    author="Dylan Araps",
    author_email="dylan.araps@gmail.com",
    description="Download and display album art for mpd tracks.",
    long_description=LONG_DESC,
    license="MIT",
    url="https://github.com/skielred/bum",
    download_url=DOWNLOAD,
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": ["bum=bum.__main__:main"]
    },
    install_requires=[
        "musicbrainzngs",
        "python-mpv",
        "python-mpd2",
    ],
    python_requires=">=3.6",
    test_suite="tests",
    include_package_data=True
)
