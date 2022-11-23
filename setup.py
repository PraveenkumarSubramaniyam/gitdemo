from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gitdemo/__init__.py
from gitdemo import __version__ as version

setup(
	name="gitdemo",
	version=version,
	description="Testing ",
	author="praveenkumarcse2211@gmail.com",
	author_email="praveenkumarcse2211@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
