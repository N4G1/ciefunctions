from setuptools import setup

setup(
    name="ciefunctions",
    version="1.0.0b4",
    packages=['tc1_97'],
    scripts=['ciefunctions.py'],
    include_package_data=True,
    package_data={'tc1_97': ['data/*', '*.css', 'MathJax-2.7.5/*']},
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'pyqt5'],
    author="Jan Henrik Wold and Ivar Farup",
    author_email="ivar.farup@ntnu.no",
    description="Desktop and web apps for computing the CIE Functions",
    license="GPL3.0",
    url="https://github.com/ifarup/ciefunctions"
)
