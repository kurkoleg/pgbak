from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
     readme = f.read()

setup(
    name='pgbak',
    version='0.1.0',
    description='DB backup, locally or to AWS S3',
    long_description=readme,
    author='Oleg Kurkovskiy',
    author_email='kurkoleg@gmail.com',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'':'src'},
)






