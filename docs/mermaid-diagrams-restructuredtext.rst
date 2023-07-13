##################################
Mermaid diagrams: reStructuredText
##################################


*****
About
*****

`Mermaid`_ is a JavaScript based diagramming and charting tool that renders Markdown-
inspired text definitions to create and modify diagrams dynamically.

By adding a ``mermaid`` directive, the `sphinxcontrib-mermaid`_ extension allows you to
embed Mermaid graphs in your documents, including general flowcharts, sequence diagrams,
gantt diagrams, and more.

The most popular chart will probably be a flowchart, see `Flowcharts - Basic Syntax`_
for an introduction.

.. _Mermaid: https://mermaid.js.org/
.. _Flowcharts - Basic Syntax: https://mermaid.js.org/syntax/flowchart.html
.. _sphinxcontrib-mermaid: https://pypi.org/project/sphinxcontrib-mermaid/


********
Examples
********

Sequence diagram
================

.. mermaid::

    sequenceDiagram
      participant Alice
      participant Bob
      Alice->John: Hello John, how are you?

Flowchart diagram
=================

.. mermaid:: _static/mermaid-example.mmd
