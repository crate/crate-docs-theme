# Mermaid diagrams


## About

[Mermaid] is a JavaScript based diagramming and charting tool that renders Markdown-
inspired text definitions to create and modify diagrams dynamically.

By adding a `mermaid` directive, the [sphinxcontrib-mermaid] extension allows you to
embed Mermaid graphs in your documents, including general flowcharts, sequence diagrams,
gantt diagrams, and more.

The most popular chart will probably be a flowchart, see [Flowcharts - Basic Syntax]
for an introduction.

[Mermaid]: https://mermaid.js.org/
[Flowcharts - Basic Syntax]: https://mermaid.js.org/syntax/flowchart.html
[sphinxcontrib-mermaid]: https://pypi.org/project/sphinxcontrib-mermaid/


## Examples

### Sequence diagram
```{mermaid}
sequenceDiagram
  participant Alice
  participant Bob
  Alice->John: Hello John, how are you?    
```

### Flowchart diagram
```{mermaid} ../_static/mermaid-example.mmd
```
