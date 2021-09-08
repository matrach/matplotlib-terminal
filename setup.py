from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='matplotlib-terminal',
    version='0.1a4',
    description='Render matplotlib plots in terminal.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/matrach/matplotlib-terminal',
    author='Maciej Matraszek',
    author_email='matraszek.maciej@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'img2unicode>=0.1a8',
    ],
    extras_require={
        'develop': [
            'pytest',
            'pytest-cov',
            'sphinx',
            'sphinx_autodoc_typehints',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    zip_safe=False)
