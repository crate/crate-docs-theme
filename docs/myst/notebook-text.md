---
# A Jupyter Notebook written in Markdown.
# https://myst-nb.readthedocs.io/
file_format: mystnb
---

(notebook-text)=

# Notebook (text-based)

The documentation can include [text-based notebooks] using [MyST-NB],
effectively bringing Jupyter technologies to Markdown.

```{code-cell} ipython3
import sys
print("this is some stdout")
print("this is some stderr", file=sys.stderr)
```

:::{tip}
See also {ref}`notebook-traditional` and {ref}`cells`.
:::


[MyST-NB]: https://myst-nb.readthedocs.io/
[text-based notebooks]: https://myst-nb.readthedocs.io/en/latest/authoring/text-notebooks.html
