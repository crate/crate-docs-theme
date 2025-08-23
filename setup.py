# -*- coding: utf-8; -*-
#
# Licensed to Crate (https://crate.io) under one or more contributor
# license agreements.  See the NOTICE file distributed with this work for
# additional information regarding copyright ownership.  Crate licenses
# this file to you under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.  You may
# obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#
# However, if you have executed another commercial license agreement
# with Crate these terms will supersede the license and you may use the
# software solely pursuant to the terms of the relevant commercial agreement.

import os
from importlib import machinery
from setuptools import setup, find_namespace_packages

pwd = os.path.join(os.path.dirname(__file__))
filepath = os.path.join(pwd, "src", "crate", "theme", "rtd", "__init__.py")
version = machinery.SourceFileLoader("theme", filepath).load_module().__version__

README = open(os.path.join(pwd, 'README.rst')).read()

setup(
    name="crate-docs-theme",
    version=version,
    description="CrateDB Documentation Theme",
    long_description=README,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Documentation",
    ],
    author="Crate.IO GmbH",
    author_email="office@crate.io",
    url="https://github.com/crate/crate-docs-theme",
    keywords="cratedb docs sphinx readthedocs",
    license="Apache License 2.0",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "furo==2025.7.19",
        "jinja2>=3,<4",
        "jupysql<0.12",
        "myst-nb<1.4",
        "myst-parser[linkify]<5",
        "oembedpy>=0.8.1,<0.9",
        "snowballstemmer<4",
        "sphinx>=7.1,<9",
        "sphinx-basic-ng==1.0.0b2",
        "sphinx-copybutton>=0.3.1,<1",
        "sphinx-design-elements==0.4.0",
        "sphinx-inline-tabs",
        "sphinx-sitemap<2.8.0", #temporarily pinned due to build warnings with 2.7.0
        "sphinx-subfigure<1",
        "sphinx-togglebutton<1",
        "sphinxext.opengraph>=0.4,<1",
        "sphinxcontrib-mermaid<2",
        "sphinxcontrib-plantuml>=0.21,<1",
        "sphinxcontrib-youtube<2",
    ],
    python_requires=">=3.9",
)
