# Licensed to Crate (https://crate.io) under one or more contributor license
# agreements.  See the NOTICE file distributed with this work for additional
# information regarding copyright ownership.  Crate licenses this file to you
# under the Apache License, Version 2.0 (the "License"); you may not use this
# file except in compliance with the License.  You may obtain a copy of the
# License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations under
# the License.
#
# However, if you have executed another commercial license agreement with Crate
# these terms will supersede the license and you may use the software solely
# pursuant to the terms of the relevant commercial agreement.


# This file provides a standard Crate documentation build system
#
# The most up-to-date version of this Makefile can be found in the
# crate-docs-style repository:
#
#   https://github.com/crate/crate-docs-style/blob/master/docs/Makefile

.EXPORT_ALL_VARIABLES:

ENV_DIR  := .venv
ENV_BIN  := $(ENV_DIR)/bin
ACTIVATE := $(ENV_BIN)/activate
PYTHON   := python3
PIP      := $(ENV_BIN)/pip3
TWINE    := $(ENV_BIN)/twine
NODE     := $(ENV_BIN)/node
NPM      := $(ENV_BIN)/npm
NODEENV  := $(ENV_BIN)/nodeenv
DIST_DIR := .dist
PYPIRC   := ~/.pypirc

NODEJS_VERSION := 18.17.0

# Default target
.PHONY: help
help:
	@ printf 'Run `make <TARGET>`, where <TARGET> is one of:\n'
	@ echo
	@ printf '\033[36m  build   \033[00m Build the package\n'
	@ echo
	@ printf '\033[36m  upload  \033[00m Upload the package to PyPI\n'
	@ echo
	@ printf '\033[36m  clean   \033[00m Clean up (e.g., remove the build'
	@ printf                           ' files)\n'
	@ echo
	@ printf '\033[36m  reset   \033[00m Reset the build system\n'

$(NODE):
	$(PIP) install nodeenv
	$(NODEENV) --python-virtualenv --node=$(NODEJS_VERSION)
	. $(ACTIVATE) && \
		npm install --global yarn

$(TWINE):
	$(PYTHON) -m venv $(ENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

.PHONY: build
build: $(TWINE)
	@ $(MAKE) clean
	@ $(MAKE) bundle-release
	. $(ACTIVATE) && \
	    $(PYTHON) -m build --outdir $(DIST_DIR)
	. $(ACTIVATE) && \
	    $(TWINE) check $(DIST_DIR)/*

.PHONY: nodejs-lts
nodejs-lts: $(NODE)

.PHONY: bundle-release
bundle-release: nodejs-lts
	. $(ACTIVATE) && \
		printf "Node.js version: "; node --version && \
		printf "Yarn version: "; yarn --version && \
		yarn install && \
		npx webpack --mode=production

.PHONY: bundle-develop
bundle-develop: setup-virtualenv nodejs-lts
	. $(ACTIVATE) && \
		printf "Node.js version: "; node --version && \
		printf "Yarn version: "; yarn --version && \
		yarn install && \
		npx webpack --mode=development $(OPTIONS)

.PHONY: bundle-watch
bundle-watch:
	$(MAKE) bundle-develop OPTIONS=--watch

.PHONY: upload
upload: $(TWINE)
	@ if test ! -d $(DIST_DIR); then \
	    $(MAKE) build; \
	fi
	@ if test ! -f $(PYPIRC); then \
	    echo 'You must configure a `$(PYPIRC)` file.'; \
	    exit 1; \
	fi
	. $(ACTIVATE) && \
	    $(TWINE) upload $(DIST_DIR)/*

.PHONY: clean
clean:
	rm -rf $(DIST_DIR)

.PHONY: reset
reset:
	rm -rf $(ENV_DIR)
	rm -rf $(DIST_DIR)

setup-virtualenv:
	@test -e $(PYTHON) || python3 -m venv $(ENV_DIR)
