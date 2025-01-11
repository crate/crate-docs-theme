---
# A Jupyter Notebook written in Markdown.
# https://myst-nb.readthedocs.io/
jupytext:
  text_representation:
    format_name: myst
---

(cell)=
(cells)=

# Cells

Widget elements that are like "editors with output".

:::{note}
_**Status:** Just written down, no special styling per CSS
has been applied yet. Contributions are welcome._
:::


## Sphinx

Those are solely based on vanilla [docutils]/[Sphinx] directives
`code` and `csv-table`, written down in MyST Markdown instead
of reStructuredText.

:::{code} sql
SELECT * FROM sometable
:::
:::{csv-table}
:header: >
:    "schema_name", "table_name", "sum(num_docs)"
:widths: 15, 10, 30

"doc", "taxi_january", 5929248
"doc", "taxi_january_bestcompression", 5929248
"doc", "taxi_january_nocolumnstore_bestcompression", 5929248
"doc", "taxi_january_nocolumnstore_noindex_bestcompression", 5929248
"doc", "taxi_january_noindex_bestcompression", 5929248
"doc", "taxi_january_nocolumnstore", 5929248
:::

:::{code} bash
antrl4
:::
:::{code} text
Downloading antlr4-4.13.2-complete.jar
ANTLR tool needs Java to run; install Java JRE 11 yes/no (default yes)? yes
Installed Java in /root/.jre/jdk-11.0.24+8-jre; remove that dir to uninstall
ANTLR Parser Generator  Version 4.13.2
:::

## IPython

Those are using [MyST-NB],
actually executing Python code,
like [doctest] is doing it.

```{code-cell} ipython3
import sys
print("this is some stdout")
print("this is some stderr", file=sys.stderr)
```

:::{important}
This actually means the documentation can include Jupyter Notebooks
now, both using the traditional .ipynb JSON file format, but also
using the .md file format, enabling [text-based notebooks].
Enjoy {ref}`notebook-text`.
:::



[docutils]: https://www.docutils.org/
[doctest]: https://docs.python.org/3/library/doctest.html
[MyST-NB]: https://myst-nb.readthedocs.io/
[Sphinx]: https://www.sphinx-doc.org/
[text-based notebooks]: https://myst-nb.readthedocs.io/en/latest/authoring/text-notebooks.html
