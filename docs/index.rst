.. updater documentation master file, created by
   sphinx-quickstart on Sun Aug 13 18:24:19 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Crude user updater documentation
===================================

Basic function to create updates from zip archives.

All you need to know
====================

Create a zip from your source directory:
::

    import updater
    updater.create_archive("src", ignore_list=updater.COMMON_FILTERS, package_name="my_super_package.zip")


Apply the update:
::

    import updater
    updater.apply_archive("my_super_package.zip", "final_destination")


.. toctree::
   :maxdepth: 4
   :caption: Contents:

   updater


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
