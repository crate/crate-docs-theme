========================================
CHANGES for Crate.io Documentation Theme
========================================

Unreleased
----------

- Changed width to 100% and max-width to 400px on .main-nav for tablet/mobile to prevent overflow on smaller devices in custom.css
- Added minWidth: 992 for sticky-sidebar to layout.html to fix scroll issues on mobile devices
- removed 60px padding in .toctree to get rid of the whitespace
- added 20px margin below to .bs-docs-sidebar so the h1 won't overlap

2019/12/19 0.7.2
----------------

- Aligned docs nav bar to the website and in regard to the latest
  product addition
- Added CrateDB Cloud on Azure
- Deleted comparison page

2019/11/08 0.7.1
----------------

- Updated top nav and bottom nav to match site
- Removed Getting Started navigation link
- Made Tutorials link un-hidden

2019/10/30 0.7.0
----------------

- Update GitHub shortcut Ctrl + e
- Add (hidden) CrateDB Tutorials project
- Update Python conf module names to reflect current docs structure

2019/10/01 0.6.0
----------------

- Add a "view on GitHub" button
- Add a key shortcut Ctrl + e to open the GitHub page.

2019/09/23 0.5.85
-----------------

- Display Cloud Getting Started link

2019/08/16 0.5.84
-----------------

- Remove title attribute from navigation links
- Upgrade docs utils to 0.1.11

2019/07/24 0.5.83
-----------------

- Add Cloud Getting Started project

2019/07/10 0.5.82
-----------------

- Fix bolding of literals in left-hand navigation menu

2019/07/09 0.5.81
-----------------

- Upgrade to docs style 0.1.10
- Improve left-hand navigation menu scrolling

2019/07/05 0.5.80
-----------------

- Add stub documentation project for testing the theme
- Add new standalone config module for documentation projects that don't appear
  in the navigation menu
- Revamp package build system
- Removed unused `docutils.conf` file
- Update package description
- Bump required Python version to 3.7
- Tidy up `.gitignore`
- Tidy up top-level documentation

2019/07/04 0.5.79
-----------------

- Improved navigation menu scroll behaviour.
- Fixed style of <code> titles in navigation menu.
- Removed mmenu.all.min.js library.
- Updated LICENSE and NOTICE.

2019/05/27 0.5.78
-----------------

- Removed Python 2 in favour of Python 3.
- Removed setuptools requirement.

2019/05/15 0.5.77
-----------------

- Link to the IoT Data Platform docs is hidden unless you are currently viewing
  those docs.

2019/05/13 0.5.76
-----------------

- Added new CrateDB Cloud IoT Data Platform docs project. This includes a new
  template config module and a change to the HTML navigation menu.

2019/04/26 0.5.75
-----------------

- Unreleased

2019/04/26 0.5.74
-----------------

- Change the ``html_context`` keys for custom js/css scripts from
  ``script_files`` to ``extra_script_files`` and from ``css_files`` to
  ``extra_css_files``.
  This change fixes a regression that was introduces in ``0.5.73`` which
  allowed the build process on RTD to "inject" their css/js using the
  ``script_files``/``css_files`` keys of the html context.

2019/04/10 0.5.73
-----------------

- Change depth of toc tree of Cloud CLI project to 2.

- Allow per-project additional script files by specifying ``script_files`` in
  the project's ``html_context`` (in ``conf.py``).

- Allow per-project additional css files by specifying ``css_files`` in
  the project's ``html_context`` (in ``conf.py``).

2019/03/19 0.5.72
-----------------

- Aligned doc footer and website footer

2019/02/04 0.5.71
-----------------

- Remove Slack button

2019/02/04 0.5.70
-----------------

- Fix sitemap

2019/01/28 0.5.69
-----------------

- Update project URLs

2019/01/22 0.5.68
-----------------

- Add Croud docs

2018/12/10 0.5.67
-----------------

- Fix link to CrateDB Cloud docs

2018/12/06 0.5.66
-----------------

- Fixed config issue

2018/12/06 0.5.65
-----------------

- Add CrateDB Cloud to navigation
- Fix support link

2018/11/27 0.5.64
-----------------

- Update navigation to match primary website

2018/10/15 0.5.63
-----------------

- Retitle Npgsql navigation link

2018/10/15 0.5.62
-----------------

- Fix .NET config module

2018/10/15 0.5.61
-----------------

- Add .NET client and fix navigation

2018/09/18 0.5.60
-----------------

- Increase SQL-99 TOC level in the side navigation

2018/09/13 0.5.59
-----------------

- Add SQL-99 docs project (hidden for now)

2018/05/30 0.5.58
-----------------

- Add admonition graphics and change admonition styles

2018/03/22 0.5.57
-----------------

- Add step to update setuptools to DEVELOP.rst
- Fixed an issue that caused the search to contain HTML in the preview

2018/03/01 0.5.56
-----------------

- Update navbar

2018/02/14 0.5.55
-----------------

- Add trailing slash to links

2018/02/13 0.5.54
-----------------

- Fix template error

2018/02/13 0.5.53
-----------------

- Added new docs project for Admin UI

2018/02/02 0.5.52
-----------------

- Added dependency to sphinx_sitemap

2018/02/01 0.5.51
-----------------

- Added new menu

2017/11/21 0.5.50
-----------------

- Correct nested list margin

2017/11/20 0.5.49
-----------------

- Adjust sidebar div styling
- Fix heading link color
- Added bottom margin to imgs

2017/11/08 0.5.48
-----------------

- Fix link

2017/11/08 0.5.47
-----------------

- Fix build for epub builder
- Add getting started docs

2017/11/03 0.5.46
-----------------

- Chop off en/latest when building alt version links

2017/10/26 0.5.45
-----------------

- Conditionally apply canonical url patch based on builder type

2017/10/25 0.5.44
-----------------

- Update canonical URLs to use "en/latest"

2017/10/25 0.5.43
-----------------

- Force canonical URL override on RTD

2017/10/09 0.5.42
-----------------

- Limit sidebar height and scroll the overflow
- Remove link styling from content headings
- Style admonition links to be more visible
- Add some bottom margin to the tables for spacing

2017/09/12 0.5.41
-----------------

- Hide mobile nav toggle on desktop viewport

2017/09/11 0.5.40
-----------------

- Improvements for mobile browsers

2017/09/05 0.5.39
-----------------

- Remove topic div border

2017/09/05 0.5.38
-----------------

- Add search results structure to jQuery function

2017/09/04 0.5.37
-----------------

- Correct HTML structure for search results
- Minor style changes

2017/09/01 0.5.36
-----------------

- Fixed the scroll jerk issue on the sidebar
- Updated the navbar to match the newer version on the website
- Expanded container layout to match newer design
- Added search documentation button to sidebar
- Improved styling of search results page
- Added custom.js and custom.css for easy front-end changes

2017/08/24 0.5.35
-----------------

- Debug release

2017/08/17 0.5.34
-----------------

- fixed and updated segment tracking code

2017/08/01 0.5.33
-----------------

- Removed debug code

2017/08/01 0.5.32
-----------------

- Debug release

2017/08/01 0.5.31
-----------------

- Debug release

2017/08/01 0.5.30
-----------------

- Debug release

2017/08/01 0.5.29
-----------------

- Dropped favicon config
- Updated canonical URL config

2017/07/18 0.5.28
-----------------

- Increase TOC depth for CrateDB guide

2017/07/18 0.5.27
-----------------

- Drop Java docs from navigation

2017/07/17 0.5.26
-----------------

- Drop Mesos docs from navigation

2017/07/10 0.5.25
-----------------

- Update navigation for docs reorganisation

2017/07/03 0.5.24
-----------------

- Fix display of literals

2017/05/02 0.5.23
-----------------

- Fix issue that caused the doc navigation to not be displayed

2017/04/25 0.5.22
-----------------

- Fix CSS filename and HTML indentation

2017/04/24 0.5.21
-----------------

- Fix CSS issues

2017/04/24 0.5.20
-----------------

- Bump version for new upload

2017/04/20 0.5.19
-----------------

- Updated header and footer to match main website

2017/02/20 0.5.18
-----------------

- Fixed issue that caused the search result links to be broken

2017/02/20 0.5.17
-----------------

- Added style for tip type admonitions

2017/01/16 0.5.16
-----------------

- Added style for caution type admonitions

2016/06/22 0.5.15
-----------------

- Conf file for mesos was missing

2016/06/22 0.5.14
-----------------

- Added menu item for mesos-framework docs

2016/05/17 0.5.13
-----------------

- Fix missing favicon

2016/05/03 0.5.12
-----------------

- Fixing menu scroll for long menus

2016/04/26 0.5.11
-----------------

- Made h4 tag style more consistent

2016/04/08 0.5.10
-----------------

- removed /stable from canonical url

2016/04/05 0.5.9
----------------
- Added padding to stop system scroll bars obscuring code

2016/03/30 0.5.8
----------------

- fixed links in footer to exclude .html also updated facebook link

2016/03/17 0.5.7
----------------

- Fixed layout issue that caused a layout overlapping of results on search page

2016/03/16 0.5.6
----------------

- Host ``searchtools.js`` in local theme since RTD has overrided the integrated
  search of Sphinx.

2016/03/01 0.5.5
----------------

- Changed docs menu to allow for new structure and 'scale' section


2016/02/15 0.5.4
----------------

- Changed Links to Downloads and Docs


2016/02/11 0.5.3
----------------

- Fixed menu expansion issue

- Changed font size


2016/01/26 0.5.2
----------------

- Code highlighting improved

- Changed menu titles

2016/01/26 0.5.1
----------------

- Changed Overview link

2016/01/26 0.5.0
----------------

- set up new layout

- Added new project configurations for crate-pdo, crate-dbal, and crate-ruby

2015/12/15 0.4.3
----------------

- Removed two links in the top nav as quick fix for new website

- Fixed the links in the footer section for the new urls

2015/09/05 0.4.2
----------------

- New section Use Cases

- updated Segment analytics snippet

- send events separate ID with extended attributes

- IP is now owned by Crate.IO GmbH

- signup for newsletter added

2015/07/17 0.4.1
----------------

- fixed broken links in page header

- removed support for Google Analytics tracking

2015/06/02 0.4.0
----------------

- updated CSS to new Crate look & feel

2015/05/26 0.3.9
----------------

- added support for LeadLander analytics

2014/12/03 0.3.8
----------------

- updated favicon

2014/11/11 0.3.7
----------------

- renamed 'Crate Data' to 'Crate'
  and 'Crate Data JDBC Driver' to 'Crate JDBC Driver'

2014/09/05 0.3.6
----------------

- make navigation highlightling follow page scrolling correctly

2014/08/19 0.3.5
----------------

- added styles for 'seealso' and 'todo' color boxes

- added docutils.conf to specify max length of field names

2014/08/07 0.3.4
----------------

- hardcoded canonical url to make documentation public on
  read the docs

2014/08/05 0.3.3
----------------

- added segment.io analytics

2014/07/31 0.3.2
----------------

- fixed internal page links so section headline is visible
  when selecting from left hand navigation

- decreased font size in version list

2014/07/29 0.3.1
----------------

- fixed not closed html tag

- load Google font from https or http depending on doc URL

2014/07/28 0.3.0
----------------

- new style to match website design

- added support for tracking via segment.io

- upgraded to google universal analytics tracking code

2014/07/03 0.2.7
----------------

- fixed css selector for code literals in tables

2014/07/03 0.2.6
----------------

- do not break table header lines and code literals in tables

2014/05/20 0.2.5
----------------

- added conf for crate jdbc driver

2014/05/19 0.2.4
----------------

- fix: linebreaks in code blocks

2014/05/12 0.2.3
----------------

- added conf for java client

2014/05/08 0.2.2
----------------

- fixed crash config

2014/05/08 0.2.1
----------------

- make urls in version dropdown absolute

2014/05/08 0.2.0
----------------

- changed package structure to crate.theme.rtd

2014/05/07 0.1.0
----------------

- Initial theme
