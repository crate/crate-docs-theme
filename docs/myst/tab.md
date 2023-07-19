# Tabs

## sphinx{design} Tabs

For basic "tabs" needs.

### Documentation
- [sphinx{design} » Tabs](inv:sd#sd-tabs)

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
