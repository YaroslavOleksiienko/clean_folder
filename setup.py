from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='This code sorts the files in a folder.',
    author='Yaroslav Oleksiienko',
    author_email='yaroslavhatepeople@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder=clean_folder.clean:main']}
)