######
Tables
######


*****
About
*****

The :ref:`sde:gridtable-directive` is a composite web element from :ref:`sde:index`.


********
Examples
********

.. sd-table::
    :widths: 2 6 4
    :row-class: top-border

    .. sd-row::
        .. sd-item:: **Table name**
        .. sd-item:: **Changes**
        .. sd-item:: **Column type changes**

    .. sd-row::
        .. sd-item:: pg_proc
        .. sd-item::
            | Added: prosupport, prokind, prosqlbody
            | Removed: protransform, proisagg, proiswindow
        .. sd-item:: proargdefaults: OBJECT[] -> STRING

    .. sd-row::
        .. sd-item:: pg_class
        .. sd-item::
            | Added: relrewrite
            | Removed: relhasoids, relhaspkey
        .. sd-item:: relacl: OBJECT[] -> STRING[]

    .. sd-row::
        .. sd-item:: pg_attribute
        .. sd-item::
            | Added: atthasmissing
            | Removed: attmissingval
        .. sd-item:: spcacl: OBJECT[] -> STRING[]


----

*This page is written in reStructuredText (rST).*
