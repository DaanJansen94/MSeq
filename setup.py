from setuptools import setup, find_packages

setup(
    name="mseq",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "biopython>=1.79",
        "numpy>=1.21.0",
        "requests>=2.26.0",
    ],
    entry_points={
        "console_scripts": [
            "mseq=mseq.mseq:main",
        ],
    },
    author="Daan Jansen",
    author_email="daan.jansen@itm.be",
    description="A tool for downloading and analyzing monkeypox virus sequences from NCBI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DaanJansen94/MSeq",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)