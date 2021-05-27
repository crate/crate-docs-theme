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
from setuptools import setup, find_packages

pwd = os.path.join(os.path.dirname(__file__))
filepath = os.path.join(pwd, "src", "crate", "theme", "rtd", "__init__.py")
version = machinery.SourceFileLoader("theme", filepath).load_module().__version__

README = open(os.path.join(pwd, 'README.rst')).read()

setup(
    name="crate-docs-theme",
    version=version,
    description="Crate Docs Theme",
    long_description=README,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Documentation",
    ],
    author="Crate.IO GmbH",
    author_email="office@crate.io",
    url="https://github.com/crate/crate-docs-theme",
    keywords="crate docs sphinx readthedocs",
    license="Apache License 2.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["crate"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Sphinx>=3.5,<5",
        "docutils==0.16",
        "sphinxcontrib-plantuml==0.21",
        "sphinx_sitemap==2.2.0",
        "sphinxext.opengraph==0.4.1",
        "sphinx-copybutton>=0.3.1,<1",
    ],
    python_requires=">=3.7",
)
