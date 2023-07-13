(design-elements-markdown)=
# Design elements: Markdown

## Grid layout, cards, badges

### Documentation
- [sphinx{design} » Grids](inv:design#sd-grids)
- [sphinx{design} » Cards](inv:design#sd-cards)
- [sphinx{design} » Badges](inv:design#badges)

### Examples

A composite component offering a title, description text, and both verbose and short tags.
It is suitable for authoring pages enumerating items with dense information, without
the maintenance nightmares of tables.

:::::::{grid} 1
:margin: 0
:padding: 0

::::::{grid-item-card}
:::::{grid} 2
:margin: 0
:padding: 0

::::{grid-item}
:columns: 8
[multihop-firmware](https://hiveeyes.org/docs/arduino/firmware/backdoor/multihop/README.html)

A flexible software breadboard for ISM RF packet radio nodes, relays, and gateways.

**Date:** 2015
**Source:** multihop.ino
::::

::::{grid-item}
:columns: 4
{bdg-primary-line}`rf69` {bdg-primary-line}`rf96` {bdg-primary-line}`lora` {bdg-primary-line}`beradio`

{bdg-success-line}`hx711` {bdg-success-line}`ds18b20` {bdg-success-line}`dht22`

{bdg-secondary-line}`ATmega328`

{bdg-info-line}`low-power`
::::

:::::
::::::
:::::::


## sphinx{design} Tabs

For basic "tabs" needs.

### Documentation
- [sphinx{design} » Tabs](inv:design#sd-tabs)

### Examples

::::{tab-set}

:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::

::::


## sphinx-inline-tabs

For more advanced "tabs" needs.

### Documentation

https://sphinx-inline-tabs.readthedocs.io/

### Examples

#### Basics
```{tab} Label1
Content 1
```

```{tab} Label2
Content 2
```

#### Code tabs
````{tab} Python
```python
print("Hello World!")
```

It's pretty simple!
````

````{tab} C++
```cpp
#include <iostream>

int main() {
  std::cout << "Hello World!" << std::endl;
}
```

More code, but it works too!
````

````{tab} Text
```none
Hello World!
```

Why not.
````

#### Synchronized
````{tab} Windows
```console
$ py -m pip install sphinx
```
````

````{tab} Unix (MacOS / Linux)
```console
$ python -m pip install sphinx
```
````

````{tab} Windows
:new-set:
```console
$ make.bat html
```
````

````{tab} Unix (MacOS / Linux)
```console
$ make html
```
````


#### Nested
````{tab} Windows
```{tab} Command prompt
`cmd.exe`
```
```{tab} Powershell
`ps2.exe`
```
````

````{tab} Unix (MacOS / Linux)

As can be seen on the other tab, the tab sets will "join" when there's
no text between different levels of tabs. Adding text between them
will space them out.

```{tab} Bash
`bash`
```
```{tab} Zsh
`zsh`
```
```{tab} Fish
`fish`
```
```{tab} Powershell
`ps2`
```
````


## Buttons

### Documentation
- [sphinx{design} » Buttons](inv:design#buttons)

### Examples
```{button-link} https://example.com
:color: primary
:shadow:
```

```{button-link} https://example.com
:color: primary
:outline:
```

```{button-link} https://example.com
:color: secondary
:expand:
```


## Icons

### Documentation
- [sphinx{design} » Icons](inv:design#icons)

### Examples

#### Octicon Icons

A coloured icon: {octicon}`report;1em;sd-text-info`, some more text.

- Alert: {octicon}`alert`
- Mention: {octicon}`mention`

#### Material Design Icons

- regular icon: {material-regular}`data_exploration;2em`, some more text
- A coloured regular icon: {material-regular}`settings;3em;sd-text-success`, some more text.
- A coloured outline icon: {material-outlined}`settings;3em;sd-text-success`, some more text.
- A coloured sharp icon: {material-sharp}`settings;3em;sd-text-success`, some more text.
- A coloured round icon: {material-round}`settings;3em;sd-text-success`, some more text.
- A coloured two-tone icon: {material-twotone}`settings;3em;sd-text-success`, some more text.
- A fixed size icon: {material-regular}`data_exploration;24px`, some more text.

#### FontAwesome Icons

- An icon {fas}`spinner;sd-text-primary`, some more text.
- An icon {fab}`github`, some more text.
- An icon {fab}`gitkraken;sd-text-success fa-xl`, some more text.
- An icon {fas}`skull;sd-text-danger`, some more text.


## Todo items

```{todo}
Foo bar baz.
```
