import setuptools

setuptools.setup(
    name="auto-audio",
    version="0.0.1",
    author="hanayong",
    description="You can upload audio files to Air force program",
    long_description=open('README.md').read(),
    url="https://github.com/hanayong",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)