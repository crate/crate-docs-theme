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


from crate.theme.rtd.conf import *

# If you update the `project` value here, you must update it in the
# `src/crate/theme/rtd/crate/sidebartoc.html` file or else Sphinx will not
# expand the sidebar TOC for this project.
project = u"CrateDB: Tutorials"
html_title = project

url_path = "docs/crate/tutorials"

# For sitemap extension
html_baseurl = "https://crate.io/%s/" % url_path

# For rel="canonical" links
html_theme_options.update(
    {
        "canonical_url_path": "%s/en/latest/" % url_path,
    }
)

ogp_site_url = html_baseurl
