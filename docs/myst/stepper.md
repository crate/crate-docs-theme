(stepper)=
# Stepper

Displays step-by-step instructions with numbered badges. Headings become steps
with anchors for [deep linking](#step-two).

## h2 header before stepper

Perhaps some intro text before stepper directive "::::::{stepper}"

:::::{stepper}
Or it can be after the directive.
The steps are defined by the first header. And only that level defines steps
afterwards.

### Step one defined with a h3 "###"

Steps can contain code blocks:

```bash
example code
```

### Step two

Steps can contain lists and admonitions:

- Item one
- Item two

:::{tip}
Example admonition.
:::

You can also use ":::{rubric}":

:::{rubric} Rubric text
:::

### Step three (a h3 header)

Steps can contain nested headings. You just have to make them one level smaller.

#### h4 header becomes a header, not a step

Content

#### h4 header 2

Content

##### h5 header

and content

### Step four (with a h3 header is again a step)

Some content.

:::::
