from setuptools import setup, find_packages

setup(
    name="noise",
    version="0.1.0",
    author="patrick thornton",
    author_email="patrick.thornton@g.harvard.edu",
    description="applies various kinds of noise to bitmaps",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Processing"
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.20.0",
        "opencv-python>=4.5.0",
        "Pillow>=8.0.0",
    ],
)
