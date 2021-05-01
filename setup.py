import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    # we don't intend to upload this to PyPi, so don't worry too much about
    # name, version etc
    name="shop-diary",
    version="0.0.2",
    description="Helps me when I'm in the garage like I'm Tony Stark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrew-candela/shop-diary",
    packages=setuptools.find_packages(),
    python_requires='>=3.8'
)
