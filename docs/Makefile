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
# crate-docs-utils repository:
#
#   https://github.com/crate/crate-docs-utils/blob/master/docs/Makefile

.EXPORT_ALL_VARIABLES:

# By default, we run commands from the the `docs` directory so that the
# commands output by `make` can be run if you copy and paste them. However, we
# must jump up to the top-level directory of the repository for two specific
# commands (see below).
#
# Because of this, we specify `TOP_DIR` and `DOCS_DIR` so that Make can find
# its way around.

# `TOP_DIR` is the top-level directory of the repository
TOP_DIR         := ..
# `DOCS_DIR` is the path to `docs` from `TOP_DIR`
DOCS_DIR        := docs
ENV_DIR         := .env
ACTIVATE        := $(ENV_DIR)/bin/activate
PYTHON          := python3.7
PIP             := $(PYTHON) -m pip
SPHINXBUILD     := sphinx-build
SPHINXAUTOBUILD := sphinx-autobuild
AUTOBUILD_OPTS  := --re-ignore '^(?!.+\.rst$$)'
BUILD_DIR       := .build
SPHINX_ARGS     := . $(BUILD_DIR)
SPHINX_OPTS     := -W -n
UTILS_JSON      := utils.json
UTILS_REPO      := https://github.com/crate/crate-docs-utils.git
UTILS_DIR       := .utils
UTILS_DIR_ROOT  := $(DOCS_DIR)/$(UTILS_DIR)
UTILS_RULES     := $(UTILS_DIR_ROOT)/utils/rules.mk
# Change to `TOP_DIR` so we can process all RST files in the repository
UTILS_MAKE      := $(MAKE) -C $(TOP_DIR) -f $(UTILS_RULES)
FSWATCH         := fswatch

# Default target
.PHONY: help
help:
	@ printf 'Crate Docs Utils\n'
	@ echo
	@ printf 'Run `make <TARGET>`, where <TARGET> is one of:\n'
	@ echo
	@ printf '\033[36m  dev    \033[00m Run a Sphinx development server that'
	@ printf                          ' builds and lints the \n'
	@ printf '\033[36m         \033[00m documentation as you edit the source'
	@ printf                          ' files\n'
	@ echo
	@ printf '\033[36m  html   \033[00m Build the static HTML output\n'
	@ echo
	@ printf '\033[36m  check  \033[00m Build, test, and lint the'
	@ printf                          ' documentation\n'
	@ echo
	@ printf '\033[36m  delint \033[00m Remove any `*.lint` files\n'
	@ echo
	@ printf '\033[36m  reset  \033[00m Reset the build cache\n'

$(ACTIVATE):
	$(PYTHON) -m venv $(ENV_DIR)
	. $(ACTIVATE) && \
	    $(PIP) install --upgrade pip
	@ # Change to `TOP_DIR` to mimic how Read the Docs does it
	. $(ACTIVATE) && cd $(TOP_DIR) && \
	    $(PIP) install -r $(DOCS_DIR)/requirements.txt

ifeq ($(UNAME),Linux)
$(VALE):
	mkdir -p $(TOOLS_DIR)
	curl -L $(VALE_URL)/$(VALE_LINUX) -o $(TOOLS_DIR)/$(VALE_LINUX)
	cd $(TOOLS_DIR) && tar -xzf $(VALE_LINUX)
endif

ifeq ($(UNAME),Darwin)
$(VALE):
	mkdir -p $(TOOLS_DIR)
	curl -L $(VALE_URL)/$(VALE_MACOS) -o $(TOOLS_DIR)/$(VALE_MACOS)
	cd $(TOOLS_DIR) && tar -xzf $(VALE_MACOS)
endif

# Parse JSON file for version
UTILS_VERSION = $(shell cat $(UTILS_JSON) | \
    python -c 'import json, sys; print(json.load(sys.stdin)["message"])')

ifeq ($(UTILS_VERSION),)
$(error No version specified in $(UTILS_JSON))
endif

ifeq ($(wildcard $(TOP_DIR)/utils/rules.mk),)
# The documentation for all other projects must install a versioned copy of the
# crate-docs-utils project
$(UTILS_DIR):
	git clone --depth=1 -c advice.detachedHead=false \
	    --branch=$(UTILS_VERSION) $(UTILS_REPO) $(UTILS_DIR)
else
# The documentation for the crate-docs-utils project fakes an install of its
# own code so that it can test itself
$(UTILS_DIR):
	mkdir -p $@
	cp -R $(TOP_DIR)/utils/* $@
endif

.PHONY: autobuild
autobuild: $(ACTIVATE)
	. $(ACTIVATE) && \
	    $(SPHINXAUTOBUILD) $(SPHINX_ARGS) $(SPHINX_OPTS) $(AUTOBUILD_OPTS) $(O)

.PHONY: lint
lint: $(UTILS_DIR)
	$(UTILS_MAKE) lint

.PHONY: lint-watch
lint-watch: $(UTILS_DIR)
	@ $(FSWATCH) .build/sitemap.xml | while read num; do \
	    $(UTILS_MAKE) lint; \
	done || true

.PHONY: dev
dev: lint
	@ if test ! -x "`which $(FSWATCH)`"; then \
	    printf '\033[31mYou must have fswatch installed.\033[00m\n'; \
	    exit 1; \
	fi
	@ # Run `autobuild` and `lint-watch` simultaneously with the `-j` flag.
	@ # Both output to STDOUT and STDERR. To make this less confusing,
	@ # `lint-watch` watches the sitemap file that Sphinx builds at the end of
	@ # each build iteration. So Sphinx should wake up first, and then the
	@ # linter. The resulting output flows quite nicely.
	$(MAKE) -j autobuild lint-watch

.PHONY: check
check: html linkcheck lint

# Needed by `sphinx-build`
.PHONY: Makefile
Makefile:

# Route unknown targets to `sphinx-build`
%: $(ACTIVATE)
	. $(ACTIVATE) && \
	    $(SPHINXBUILD) -M $@ $(SPHINX_ARGS) $(SPHINX_OPTS) $(O)

.PHONY: delint
delint: $(UTILS_DIR)
	$(UTILS_MAKE) delint

.PHONY: reset
reset:
	rm -rf $(ENV_DIR)
	rm -rf $(BUILD_DIR)
	rm -rf $(UTILS_DIR)
