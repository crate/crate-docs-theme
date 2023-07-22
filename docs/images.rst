==================
Images and figures
==================

.. highlight:: rst

Introduction
============

reStructuredText offers two different roles to embed images, the ``.. image``
and the ``.. figure`` role. For more information, see
`reStructuredText Directives » Images`_.

.. _reStructuredText Directives » Images: https://docutils.sourceforge.io/docs/ref/rst/directives.html#images


Image using "``image``" role
============================


.. _image-vanilla:

Vanilla
-------

.. image:: https://unsplash.com/photos/GWcYFSG7HIo/download?force=true&w=640
    :target: https://unsplash.com/photos/GWcYFSG7HIo/download?force=true&w=640
    :alt: alternate text

::

    .. image:: https://unsplash.com/photos/GWcYFSG7HIo/download?force=true&w=640
        :target: https://unsplash.com/photos/GWcYFSG7HIo/download?force=true&w=640
        :alt: alternate text


.. _image-scaling:

Scaling 50%
-----------

For scaling an ``.. image``, the size of the image must be able to be
determined. Either, the image is stored locally, or the corresponding
``:height:`` / ``:width:`` bits have to be announced.

.. image:: https://unsplash.com/photos/GWcYFSG7HIo/download?force=true&w=640
    :target: https://unsplash.com/photos/GWcYFSG7HIo/download?force=true&w=640
    :height: 427px
    :width: 640px
    :scale: 50%

::

    .. image:: https://unsplash.com/photos/GWcYFSG7HIo/download?force=true&w=640
        :target: https://unsplash.com/photos/GWcYFSG7HIo/download?force=true&w=640
        :height: 427px
        :width: 640px
        :scale: 50%


Image using "``figure``" role
=============================

.. _figure-vanilla:

Vanilla
-------

.. figure:: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
    :target: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
    :alt: alternate text

::

    .. figure:: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
        :target: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
        :alt: alternate text


.. _figure-caption:

With caption
------------

.. figure:: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
    :target: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
    :alt: alternate text

    This is the caption of the image.

::

    .. figure:: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
        :target: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
        :alt: alternate text

        This is the caption of the image.


.. _figure-legend:

With legend
-----------

.. figure:: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
    :target: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
    :alt: alternate text

    The legend consists of all elements after the caption.
    In this case, the legend consists of this paragraph and the following table:

    +-----------------------+-----------------------+
    | Symbol                | Meaning               |
    +=======================+=======================+
    | 🏕️                    | Campground            |
    +-----------------------+-----------------------+
    | 🌊                    | Lake                  |
    +-----------------------+-----------------------+
    | 🗻                    | Mountain              |
    +-----------------------+-----------------------+

::

    .. figure:: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
        :target: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
        :alt: alternate text

        The legend consists of all elements after the caption. In this case,
        the legend consists of this paragraph and the following table:

        +-----------------------+-----------------------+
        | Symbol                | Meaning               |
        +=======================+=======================+
        | 🏕️                    | Campground            |
        +-----------------------+-----------------------+
        | 🌊                    | Lake                  |
        +-----------------------+-----------------------+
        | 🗻                    | Mountain              |
        +-----------------------+-----------------------+


.. _figure-scaling:

Scaling 50%
-----------

For scaling a ``.. figure``, configuring ``:figwidth: 50%`` might be
sufficient, even without knowing about the original image dimensions.

.. figure:: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
    :target: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
    :figwidth: 50%

::

    .. figure:: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
        :target: https://unsplash.com/photos/NN15NFflk90/download?force=true&w=640
        :figwidth: 50%
