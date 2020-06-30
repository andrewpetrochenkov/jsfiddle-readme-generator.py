import setuptools

setuptools.setup(
    name='jsfiddle-readme-generator',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
