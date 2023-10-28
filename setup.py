import sys
from setuptools import setup, find_packages

setup(
    name = "multijq",
    version = "0.1",
    description = "runs multiple jq selectors as one",
    author = "Sonny S. Kothapally",
    author_email = "me@sonnyksimon.com",
    url='https://github.com/sonnyksimon/multijq/blob/master/vendor/multijq.py',
    classifiers=[],
    license='AGPLv3',
    packages=find_packages(),
    py_modules=['multijq'],
    include_package_data=True,
    zip_safe=False
)