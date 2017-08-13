Crude user updater
==================

Package to update the program of your users to the latest version using a simple archive and an ignore list.

Create a zip from your source directory:
::

    import updater
    updater.create_archive("src", ignore_list=updater.COMMON_FILTERS, package_name="my_super_package.zip")


Apply the update:
::

    import updater
    updater.apply_archive("my_super_package.zip", "final_destination")
