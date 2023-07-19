# Tables


## About

The [](inv:sde#gridtable-directive) is a composite web element from [](inv:sde:*:label#index).


## Examples

::::{sd-table}
:widths: 2 6 4
:row-class: top-border

:::{sd-row}
```{sd-item} **Table name**
```
```{sd-item} **Changes**
```
```{sd-item} **Column type changes**
```
:::

:::{sd-row}
```{sd-item} pg_proc
```
```{sd-item}
Added: prosupport, prokind, prosqlbody
<br>
Removed: protransform, proisagg, proiswindow
```
```{sd-item} proargdefaults: OBJECT[] -> STRING
```
:::

:::{sd-row}
```{sd-item} pg_class
```
```{sd-item}
Added: relrewrite
<br>
Removed: relhasoids, relhaspkey
```
```{sd-item} relacl: OBJECT[] -> STRING[]
```
:::

:::{sd-row}
```{sd-item} pg_attribute
```
```{sd-item}
Added: atthasmissing
<br>
Removed: attmissingval
```
```{sd-item} spcacl: OBJECT[] -> STRING[]
```
:::

::::


---

_This page is written in Markedly Structured Text (MyST Markdown)._
