=======
CHANGES
=======


Unreleased
----------


2024/04/06 0.31.0
-----------------
- Fix missing CI colors to align with the main website
- Update icons with the corresponding colors
- Introduce a secondary color for improved accessibility
- Small improvement for the version/feedback dropdown on mobile
- Remove intersphinx mappings to ``crate-howtos`` and ``crate-tutorials``,
  they have been converged into ``cratedb-guide``.
- Update to sphinx-design-elements 0.3.0


2024/03/05 0.30.0
-----------------

- Replaced ``Poppins`` font with ``Montserrat`` for H1
- Removed legacy ``.woff`` font-files
- Update SQL-99 config (``html_baseurl``, ``url_path``
  and ``canonical_url_path``)
- Removed ``webflow.js``, artifacts from the abandoned 
  feedback box and rating system, removed unused css
- Added "Guides and Tutorials" section


2024/01/25 0.29.10
------------------

- Removed reference to "SQL-99 Complete, Really", and
  prepare phasing it out from the cratedb.com domain.
  It will be published to https://sql-99.readthedocs.io/ instead.
- Removed HubSpot CTA from SQL-99 header
- Decluttered/separated SQL-99 footer


2023/12/07 0.29.9
-----------------

- Updated SQL-99 CTAs
- Updated unsplash profile URL to fix 404
- Tracking: Removed Segment and replaced it with Google Tagmanager


2023/09/28 0.29.8
-----------------

- Primary navigation: Use ``maxdepth=2`` for serving "CrateDB Cloud"
  That means, only pull headings up to the second level into the menu.
  Thanks, @proddata.
- Search: Added ``autofocus`` to search input for better usability.
  Thanks, @msbt.


2023/09/19 0.29.7
-----------------

- Stop displaying the edit/view source link on synthetic pages, for example,
  the ``search.html`` page. Thanks, @msbt.
- Changed domain from ``crate.io`` to ``cratedb.com``


2023/09/06 0.29.6
-----------------

- Add version chooser JavaScript helpers derived from ``pydata-sphinx-theme``.
  Thanks, @drammock.


2023/09/01 0.29.5
-----------------

- Adjust OpenGraph settings: Logo image, description length, "first image" use.
  Thanks, @proddata and @msbt.


2023/08/30 0.29.4
-----------------

- Improve primary navigation on the database driver section once more


2023/08/30 0.29.3
-----------------

- Fix CSS: Remove font size of blockquote override. Thanks, @msbt.
- Improve version chooser: Remove ambiguous link to root document.
  Thanks, @hlcianfagna.
- Bring back lost navigation items to database drivers. Thanks,
  @proddata.


2023/08/11 0.29.2
-----------------

- Fix minor regression on admonitions
- Fix page tools positioning


2023/08/08 0.29.1
-----------------

- Fix margin on page tools element
- Modernize and fix JS and CSS includes
- Fix pagetools dropdown: Group elements to define mutual toggle-opening.
  Thanks, @kojinkai and @msbt.
- Improve version chooser to use the same page when switching versions.
  Thanks, @hlcianfagna.
- Fix text alignment with sphinx-togglebutton. Thanks, @msbt.


2023/08/03 0.29.0
-----------------

- Edit primary navigation in left sidebar

  - "CrateDB Cloud" documentation has been bundled into a single repository, now
    located at ``/docs/cloud``
  - Add link to "Community" and "Integration tutorials"
  - Rename ``Install CrateDB`` to ``Install``, and ``Reference`` to ``CrateDB Reference``
  - Improve appearance of bottom section

- Consolidated Cloud Docs: Adjust intersphinx root references

  - Those project references have been dissolved:
    ``cloud-reference``, ``cloud-tutorials``, and ``cloud-howtos``
  - The new canonical intersphinx project reference is just ``cloud``

- UI: Increase z-index of feedback chooser content
- Update jquery to 3.7.0
- Update jinja2 to <3.2


2023/08/01 0.28.2
-----------------

- Adjust footer navigation after web site update. Thanks, @msbt.


2023/07/29 0.28.1
-----------------

- Fix admonition content styles for links and item lists
- Fix version chooser enablement
- Update to Sphinx ``sphinx>=4.6,<7``


2023/07/27 0.28.0
-----------------

- Add modern components from the Sphinx ecosystem: myst-parser, sphinx-design,
  sphinx-inline-tabs, sphinx-subfigure, sphinx-togglebutton, sphinxcontrib-mermaid.
- Refactor GitHub feedback component to separate files
- Migrate version chooser component to sphinx-design dropdown
- Use compact variant of GitHub feedback component at the top of the page
- Remove external links indicator
- Improve visual appearance of admonition components
- Add new ``cloud-docs`` documentation project


2023/05/15 0.27.1
-----------------

- Removed ``code``-tag from a mobile media query to fix headlines font-sizes


2023/04/18 0.27.0
-----------------

- Change Crate.io logo to CrateDB
- Remove Crate.io footer logo
- Update Favicons
- Update the ESI fallback links in case we disable it at some point
- Use relative links to pages
- Update opengraph image
- Enable meta description via ``ogp_enable_meta_description = True``


2022/12/29 0.26.5
-----------------

- Fix wheel package.


2022/12/29 0.26.4
-----------------

- Fix visual appearance of Intersphinx references per ``xref`` CSS.
  Don't render links in bold text when using custom label. Happens,
  for example, with ``:class:dictionaries <py:dict>``.


2022/09/05 0.26.3
-----------------

- SQL-99: Replace regular buttons with HubSpot CTAs
- Fix error with switchover to ``js-cookie`` library


2022/07/25 0.26.2
-----------------

- Fix ``js-cookie`` library import


2022/07/25 0.26.1
-----------------

- Fix webpack expose configuration for ``js-cookie`` library


2022/07/22 0.26.0
-----------------

- Fix copying multi-line console snippets with ``sphinx-copybutton``
- Update JavaScript dependencies across the board
- Replace ``jquery-cookie`` with ``js-cookie``
- Add missing ``loading="lazy"`` to footer images


2022/07/13 0.25.0
-----------------

- Bump runtime dependency versions
- Bring CI setup up to speed
- Upgrade to Sphinx 5
- Search: Add message if no results were found
- Search: Don't show if ``googleapis.com`` doesn't respond
- SEO: Change Open Graph description length from 300 to 150 characters
- UI: Make tables scroll horizontally on devices with <991px width
- UI: Remove whitespace at the top on SQL-99 on devices <991px width
- UI: Remove column layout from field lists on devices <560px width


2022/06/23 0.24.5
-----------------

- Fix ``proxied_static_path`` context variable following an RTD update


2022/05/17 0.24.4
-----------------

- Another hide navbar when opening anchor links fix


2022/05/16 0.24.3
-----------------

- Fix dropdown menu overlap
- Hide navbar when opening anchor links fix


2022/05/16 0.24.2
-----------------

- Add height attribute to crate.io logo to avoid CLS
- Hide navbar when opening anchor links


2022/05/04 0.24.1
-----------------

- Fix sidebar toc collapse setting


2022/05/04 0.24.0
-----------------

- Fix padding-top for SQL-99 documentation. Thanks, @msbt!
- Update Open Graph image. Thanks, @msbt!
- Improve menu structure of left-hand sidebar. Thanks, @jayeff!


2022/04/05 0.23.0
-----------------

- Fix path to ERDF footer logo
- Avoid reflow on content div element when loading the page
- Disable smooth scrolling


2022/03/31 0.22.3
-----------------

- SQL-99: Fix hover and active states of search button and search input field


2022/03/30 0.22.2
-----------------

- Style: Don't uppercase text, it doesn't look good with the new font


2022/03/30 0.22.1
-----------------

- Fix typo within "SQL-99 Complete, Really"
- Add an option to adjust the ``html_context`` of individual projects,
  for disabling the GitHub feedback box on the SQL-99 project.


2022/03/29 0.22.0
-----------------

- Add ``html_context`` variable to main configuration blueprint
- Fixed mobile view on ``search.html``
- Provide different design for "SQL-99 Complete, Really" in order to more clearly
  separate it from the other documentation projects
- Use Sphinx-native search for "SQL-99 Complete, Really"
- Change primary font to ``Inter`` and secondary to ``Poppins``, remove ``Blender``
- Prevent console errors when no navbar is available
- Disable GitHub feedback box on the SQL-99 project
- Fix regression: Bring back ``pygments.css`` in ``base.html``
- Visually hide injected footer (RTD-native version chooser) after enabling RTD API access


2022/03/25 0.21.4
-----------------

- Adjust ``proxied_api_host`` once more to fix RTD API access in reverse proxy
  scenarios


2022/03/25 0.21.3
-----------------

- Mitigate double include of ``pygments.css``
- Adjust ``proxied_api_host`` to make RTD footer and version data injection work
  in reverse proxy scenarios
- Adjust dependencies to use Sphinx<4 and Jinja2<3.1


2022/03/01 0.21.2
-----------------

- Search: Don't trigger search without expression
- Search: Make navigation work even on ``search.html``
- Search: Only load ``search.js`` when actually visiting the search page
- Adjust background color of version chooser


2022/03/01 0.21.1
-----------------

- Fix search


2022/03/01 0.21.0
-----------------

- New header (hides when scrolling down, comes back when scrolling up)
- Revamped search (added pagination, number of results, source)


2022/02/15 0.20.1
-----------------

- Fix inline Google Search API request


2022/02/15 0.20.0
-----------------

- Added ``google_search_api_key``, ``google_search_cx_id`` and the corresponding
to environment variables to ``init.py`` and ``theme.conf`` to improve search
- Added HubSpot newsletter footer include


2021/12/07 0.19.1
-----------------

- Fix for promo header


2021/12/06 0.19.0
-----------------

- Updated logo, favicon, icons, fonts and colors for design refresh
- Added promo header (``notif-include``) in ``navbar.html``
- Re-added newsletter in ``footer.html`` placeholder for testing


2021/11/09 0.18.0
-----------------

- Updated/added ESI links/css for navi-header/footer to include HubSpot pages
- Added ``theme_tracking_hubspot_id`` and ``TRACKING_HUBSPOT_ID`` to
  ``init.py`` and ``theme.conf``
- Footer now includes GitHub stars


2021/10/12 0.17.0
-----------------

- Updated fallback header and footer navi
- Included a higher res ERDF image


2021/08/26 0.16.1
-----------------

- Fix "align-left" and "align-right" directives: Don't use bold text on them.
- Fix sphinx-copybutton appearance.


2021/08/06 0.16.0
-----------------

- Improve contrast of highlighted code examples
- Harmonize heading styles


2021/06/18 0.15.4
-----------------

- Switch sphinx-copybutton cursor to pointer
- Improve sphinx-copybutton: Enable copying empty lines


2021/06/07 0.15.3
-----------------

- Add ``|striptags`` to the Segment titles for proper sanitizing
- Improve version pinning


2021/05/28 0.15.2
-----------------

- Improve sphinx-copybutton: Also handle ``PS>`` prompt for Powershell
- Improve top and bottom margins for headings


2021/05/27 0.15.1
-----------------

- Fix some client docs intersphinx URLs
- Adjust style of highlighted codeblocks: Border, border radius and shadow
- Improve OpenGraph `og:url` computation
- Fix ``Uncaught TypeError: $.cookie is not a function``
- Fix version dropdown by re-adding "Webflow: Front-end site library"


2021/05/26 0.15.0
-----------------

- Minor CSS fixup for glossary link
- Upgrade to crate-docs 2.0.0
- Permit installation on Sphinx 4
- Add intersphinx mapping for cross referencing documentation across different
  repositories
- Improve bundling of custom JavaScript and CSS assets
- Fix the docs title for Segment.io / GA tracking
- Add ESI snippets for a dynamic promotion header and newsletter footer
- Improve margins and rename section class to ``w-canvas`` for proper tagging
- Add extension "sphinxcontrib.plantuml"
- Add extension "sphinxext.opengraph"
- Add "sphinx-copybutton" extension
- Use Pygments style "material" for code highlighting
- Add `doing_docs` config module (hidden menu item)


2021/03/18 0.14.0
-----------------

- Fix list styling in admonition blocks
- Glossary links are now styled black with a dotted underline


2021/03/15 0.13.3
-----------------

- Fix a typo (character case) in `sidebartoc.html` causing the TOC to not
  display for the Cloud How-Tos project


2021/03/15 0.13.2
-----------------

- Preloading the full star of the rating system to prevent empty stars
- Added a note about ``custom.css`` and ``custom.js``
- Fix sidebar TOC . Previously, Sphinx was not expanding the sidebar TOC for
  both how-to projects.


2021/02/03 0.13.1
-----------------

- Added meta description to index.rst for testing
- Properly aligned footer container with the others
- Changed crate.io logo from png to svg
- Changed to svg stars from characters so all platforms look the same
- Changed menu from fontawesome bars to spans
- Fixed minor regressions from last update (borders, indents)
- Excluded internal links from external link icon
- Removed fontawesome.js


2021/01/26 0.13.0
-----------------

- SEO: Added `rel="noopener"` to Github links (links to cross-origin
  destinations are unsafe)
- Updated/removed Bootstrap and jQuery packages (nine vulnerabilities detected)
- SEO: Added `height: auto;` to the logo css (lighthouse cought a wrong AR)
- SEO: Added alt & title tags to logos in header and footer
- Moved esi to the correct position
- SEO: Added dns-prefech/preconnect to googleapis.com and cdn.crate.io
- Updated version tag for css/js in `base.html` for cleaner caches
- SEO: Added language `xml:lang="en" lang="en"`
- Added Favicon
- SEO: Preloading Font
- SEO: Minified/Combined static js/css files (except custom and doctools)
- SEO: Removed `maximum-scale=1` from meta viewport to allow zooming
- Added new rating feature below the feedbackbox
- SEO: Changed h3 to h2 for feedbackbox and new rating
- Fixed a minor css error in `crateio.css` and added `font-display: swap;`
- Fixed colors of the `Toggle Doc Menu` (mobile)
- Add left-margin to all lists
- Fix paragraph margins for lists using the "open" class


2020/12/01 0.12.0
-----------------

- Permit installation with more recent versions of Sphinx by relaxing strict
  dependency on ``Sphinx==1.8.5``
- Update to ``sphinxcontrib-plantuml==0.19``


2020/10/22 0.11.0
-----------------

- Added WordPress navi as edge side include via Varnish
- Added bottom margin to code highlights

2020/10/06 0.10.17
------------------

- New icons and colors for admonitions


2020/09/17 0.10.16
------------------

- Dropped unnecessary versioned sphinx requirement specified by docs project
- Changed url for `Try CrateDB` to the CrateDB Cloud anchor
- Excluded images from external link indicator


2020/09/02 0.10.15
------------------

- Fix typo in URL for Clients & Tools


2020/09/01 0.10.14
------------------

- Add class to exclude feedback box links from external link indicator


2020/08/31 0.10.13
------------------

- The sitemap_url_scheme setting is now manually configured so that sitemap
  links work correctly when built locally and on Read The Docs.


2020/08/27 0.10.12
------------------

- Change sitemap name to `site.xml`
- Add page title to issue search to filter out false positives for root
  index.html page (and potentially other scenarios)
- Switch default issue label from "area: docs" to "team: tech writing"
- Fix subheading link styles so they are consistent with <h1> elements


2020/08/25 0.10.11
------------------

- Change sitemap name to `crate.xml` to see if that works with RTD


2020/08/25 0.10.10
------------------

- Add padding-top to the current menu item
- Change link color to fit the new one on crate.io
- Add external link indicator


2020/08/24 0.10.9
-----------------

- Add configuration to change sitemap name


2020/08/24 0.10.8
-----------------

- Remove html_extra_path for crate-howtos.py


2020/08/20 0.10.7
-----------------

- Add config to implement custom robots.txt


2020/08/18 0.10.6
-----------------

- Update docs projects config files to match sphinx-sitemap upgrade


2020/08/18 0.10.5
-----------------

- Update sphinx-sitemap to latest version


2020/08/04 0.10.4
-----------------

- Updated GitHub label to "area: docs"
- Added comparison page
- Rearranged partner page
- Removed comparison from footer


2020/07/23 0.10.3
-----------------

- Updated navbar and footer to match main website


2020/07/22 0.10.2
-----------------

- Downgraded Sphinx dependency to 1.8.5 (matches new RTD default)


2020/07/20 0.10.1
-----------------

- Updated dependency to Sphinx 3.1.2


2020/06/22 0.10.0
-----------------

- Removed hardcoded segment tracking ID. Instead, this is now settable in the
  project's ``conf.py``, or by exporting the ``TRACKING_SEGMENT_ID``
  environment variable during the build.


2020/06/04 0.9.6
----------------

- Fixed links in pre-filled text in docs issue template
- Improved Feedback section (one fetch instead of two) and updated tracking


2020/05/18 0.9.5
----------------

- Fixed project titles


2020/05/06 0.9.4
----------------

- Fixed search string
- Fixed use of HTML suffix


2020/05/06 0.9.3
----------------

- New issues now come with pre-filled template text
- Feedback section now only shows issues that relate to the current page
- Re-enable GitHub Feedback section


2020/05/04 0.9.2
----------------

- Disabled GitHub Feedback section for more testing


2020/05/04 0.9.1
----------------

- Added GitHub Feedback section


2020/04/29 0.9.0
----------------

- Added new Clients and Tools project to CrateDB section
- Split off links to client library docs projects and drop "Clients" menu item


2020/03/31 0.8.2
----------------

- Deleted unused modules
- Fixed template logic


2020/03/30 0.8.1
----------------

- Moved Admin UI and Crash into the CrateDB section.


2020/03/30 0.8.0
----------------

- Updates for docs reshuffle, including nav bar update and module name changes.


2020/01/22 0.7.5
----------------

- Edited a function that shows/hides the toggled docs menu on mobile.
- Changed ``z-index`` of ``header.header-nav`` so ``version-select-container``
  won't overlap on mobile
- Changed ``Edit on GitHub`` link from ``blob`` to ``edit`` in ``layout.html``


2020/01/21 0.7.4
----------------

- Removed a function that hides the toggled docs menu on mobile.


2020/01/20 0.7.3
----------------

- Changed ``width`` to ``100%`` and ``max-width`` to ``400px`` on
  ``.main-nav`` for tablet and mobile to prevent overflow on smaller
  devices in ``custom.css``.
- Added ``minWidth: 992`` for ``sticky-sidebar`` to ``layout.html`` to
  fix scroll issues on mobile devices.
- Removed ``60px`` padding in ``.toctree`` to get rid of the whitespace.
- Added ``20px`` margin below to ``.bs-docs-sidebar`` so the ``h1`` won't
  overlap.


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
  This change fixes a regression that was introduced in ``0.5.73`` which
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
