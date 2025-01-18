from setuptools import setup, find_packages

setup(
    name='102203821_topsis',
    version='0.1',
    description='TOPSIS implementation for ranking alternatives based on multiple criteria',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/topsis',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'openpyxl',  # for reading Excel files
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
