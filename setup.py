#!/usr/bin/env python
import codecs
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    """Open a related file and return its content."""
    with codecs.open(os.path.join(here, filename), encoding='utf-8') as f:
        content = f.read()
    return content

README = read_file('README.rst')
CHANGELOG = read_file('CHANGELOG.rst')


setup(
    name="django-tinymce",
    version="4.0.0",
    packages=find_packages(),
    include_package_data=True,
    author="Aljosa Mohorovic",
    author_email="aljosa.mohorovic@gmail.com",
    description=("A Django application that contains a widget to render a "
                 "form field as a TinyMCE editor."),
    long_description=README + "\n\n" + CHANGELOG,
    license="MIT License",
    keywords="django widget tinymce",
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "django>=3.2",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    platforms=['any'],
    url="https://github.com/jazzband/django-tinymce",
    project_urls={
        "Homepage": "https://github.com/jazzband/django-tinymce",
        "Documentation": "https://django-tinymce.readthedocs.org/",
        "Changelog": "https://github.com/jazzband/django-tinymce/blob/master/CHANGELOG.rst",
    },
)
