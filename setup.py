from setuptools import setup

def readme():
    with open('README.rst.example') as f:
        return f.read()

(name='marble',
    version='0.1',
    description=('A python library to study socio-spatial stratification '+
                 'in cities'),
    long_description=readme(),
    url='http://github.com/scities/marble',
    author='Rémi Louf',
    author_email='remi.louf@sciti.es',
    license='BSD',
    packages=['marble'],
    setup_requires=[
        'networkx',
        'shapely'
        ],
    testt_suite='nose.collector',
        tests_require=['nose'],
    zip_safe=False)
