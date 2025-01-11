---
# A Jupyter Notebook written in Markdown.
# https://myst-nb.readthedocs.io/
file_format: mystnb
---

(notebook-text)=

# Notebook (text-based)

The documentation can include [text-based notebooks] using [MyST-NB],
effectively bringing Jupyter technologies to Markdown.

## Basics

```{code-cell} ipython3
import sys
print("this is some stdout")
print("this is some stderr", file=sys.stderr)
```

:::{tip}
See also {ref}`notebook-traditional` and {ref}`cells`.
:::

## SQL Magics

[JupySQL], the successor of [ipython-sql], enables running SQL in Jupyter/IPython
via `%sql` and `%%sql` magics.

```{code-cell} ipython3
# Acquire data.
!pip --quiet install csvkit
!curl -s -L -O https://github.com/wireservice/csvkit/raw/refs/heads/master/examples/realdata/acs2012_5yr_population.csv
!rm -f population.db
!csvsql --db sqlite:///population.db --insert acs2012_5yr_population.csv
```
```{code-cell} ipython3
# Run query using JupySQL.
%reload_ext sql
%sql sqlite:///population.db
%sql SELECT * FROM acs2012_5yr_population ORDER BY total_population DESC LIMIT 10;
```

:::{note}
Here, we are using SQLite, in order not to make `sqlalchemy-cratedb` a
dependency of the documentation theme. An example using CrateDB can be
explored at [CrateDB Examples: notebook/jupyter].
:::

:::{todo}
Rendering the result table has unfortunate output when using dark mode.
Please switch to light mode instead.
:::


[CrateDB Examples: notebook/jupyter]: https://github.com/crate/cratedb-examples/tree/main/notebook/jupyter
[ipython-sql]: https://github.com/catherinedevlin/ipython-sql
[JupySQL]: https://jupysql.ploomber.io/
[MyST-NB]: https://myst-nb.readthedocs.io/
[text-based notebooks]: https://myst-nb.readthedocs.io/en/latest/authoring/text-notebooks.html
