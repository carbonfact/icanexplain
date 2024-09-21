# Kilsbergen

A clean [MkDocs][mkdocs] theme.

This theme is designed for [Tako][tako], [Pris][pris], and [Noblit][noblit].
It is not flexible on purpose: it supports everything I need, and nothing more.

## Demos

 * [Musium documentation][musium-docs]
 * [Noblit documentation][noblit-docs]
 * [Pris documentation][pris-docs]
 * [RCL documentation][rcl-docs]
 * [Squiller documentation][squiller-docs]
 * [Tako documentation][tako-docs]

## Features

 * Responsive design
 * Zero javascript

## Usage

One easy way to use this theme, is to add it as a Git submodule to your `docs`
directory, e.g. at `docs/theme`. Then add the following in your `mkdocs.yml`:

```yaml
theme:
  name: null
  custom_dir: docs/theme
```

This theme requires MkDocs 1.1 or later. For earlier versions, delete this
`README.md` to work around [this bug][readmebug].

To enable anchors next to section headings, add the following to your
`mkdocs.yml`:

```yaml
markdown_extensions:
  - toc:
      permalink: true
      permalink_title: null
```

To enable syntax highlighting, ensure that `pygmentize` is available, and add
the following to your `mkdocs.yml`:

```yaml
markdown_extensions:
  - codehilite
```

See also [the python-markdown list of extensions][exts].

[readmebug]: https://github.com/mkdocs/mkdocs/issues/1766
[exts]: https://python-markdown.github.io/extensions/

## License

Kilsbergen is licensed under the [Apache 2.0][apache2] license. In the generated
documentation, it is fine to just link to this readme from a comment.

[apache2]:       https://www.apache.org/licenses/LICENSE-2.0
[mkdocs]:        https://www.mkdocs.org/
[musium-docs]:   https://docs.ruuda.nl/musium/
[noblit-docs]:   https://docs.ruuda.nl/noblit/
[noblit]:        https://github.com/ruuda/noblit
[pris-docs]:     https://docs.ruuda.nl/pris/
[pris]:          https://github.com/ruuda/pris
[rcl-docs]:      https://docs.ruuda.nl/rcl/
[squiller-docs]: https://docs.ruuda.nl/squiller/
[tako-docs]:     https://docs.ruuda.nl/tako/
[tako]:          https://github.com/ruuda/tako
