from setuptools import setup

def readme():
    with open('README.rst.example') as f:
        return f.read()

setup(
    name='marble',
    version='1.0',
    description=('Study residential segregation, explore its different dimensions.'),
    url='http://github.com/scities/marble',
    author='Remi Louf',
    author_email='remi.louf@sciti.es',
    license='BSD',
    packages=['marble'],
    install_requires=[
        'networkx',
        'shapely'
        ],
    testt_suite='nose.collector',
    tests_require=['nose'],
    zip_safe = False,
)
