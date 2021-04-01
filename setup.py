from setuptools import setup, find_packages

setup(
    name = 'degubi/py-seq',
    version = '1.1.1',
    author = 'Degubi',
    description = 'Small python functional sequence processing library',
    url = 'https://github.com/Degubi/Py-Seq',
    packages = find_packages(exclude = ('tests')),
    license = 'Free for all use. Contribute back if you can :)',
    python_requires = '>=3.6'
)