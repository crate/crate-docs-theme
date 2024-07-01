# Vendored Furo styles and scripts

## About

This theme derives from [sphinx-basic-ng], but needs a few components from
[Furo]. For example, the menu builder from Furo's `navigation.py` is made
available to the HTML context via `ng_navigation_tree`.

Therefore, it needs to vendorize a few styles. It can not take the whole
thing, because Furo's colors currently interfere with the colors provided
by the theme's styles.

```{todo}
Completely migrate to Furo's color system?
```

## License

Furo's license is the MIT license. 
> Copyright (c) 2020 Pradyun Gedam <mail@pradyunsg.me>


[Furo]: https://github.com/pradyunsg/furo
[sphinx-basic-ng]: https://github.com/pradyunsg/sphinx-basic-ng
