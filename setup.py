import setuptools

setuptools.setup(
    name="protontricks",
    version="0.1.0",
    description="Protontricks",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/Matoking/protontricks",
    author="Matoking",
    author_email="janne.pulkkinen@protonmail.com",
    license="GPL-3.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
)
    # This is considered deprecated since Python wheels don't provide a way
    # to install package-related files outside the package directory
    # https://packaging.python.org/guides/packaging-namespace-packages/#namespace-packages
