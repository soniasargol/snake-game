import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

reqs = ['pygame']
setuptools.setup(
    name="snake-game",
    version="0.1",
    author="Sonia Sargolzaei",
    author_email="sousargol@gmail.com",
    description="Simple version of snake game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soniasargol/snake-game",
    license='',
    install_requires=reqs,
    packages=setuptools.find_packages()
)
