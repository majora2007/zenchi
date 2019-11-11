from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="zenchi",
    packages=["zenchi", "zenchi.mappings"],
    version="1.0.0",
    license="MIT",
    description="python interface for communication with AniDB API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="fnzr",
    author_email="5471818+fnzr@users.noreply.github.com",
    url="https://github.com/fnzr/zenchi",
    download_url="https://github.com/fnzr/zenchi/archive/v1.0.0.tar.gz",
    keywords=["anime", "anidb", "udp api"],
    install_requires=["environs", "pymongo", "pycryptodome"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
    ],
)