from distutils.core import setup

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='ldappr',
    version='0.1',
    packages=['ldappr', 'ldappr.test'],
    install_requires=['python-ldap'],
    url='https://github.com/nanu2/ldappr',
    license='ICS',
    author='Mike Helderman',
    author_email='mike.helderman@gmail.com',
    description='Wrapper around python-ldap.',
    long_description=long_description
)