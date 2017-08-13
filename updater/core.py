# -*- coding: utf-8 -*-
""" Core functions of the updater. """


import os
import re
import zipfile

from . import helpers

# Authorship information.
__author__ = "Sébastien Mathieu"
__version__ = "1.0.0"


def create_archive(path, output_path=None, ignore_list=None, package_name=None, to_remove=None,
                   compression=zipfile.ZIP_DEFLATED):
    """ Create a zip archive.

        :param path: Path to the folder to create archive from.
        :param output_path: Path to the output folder.
        :param ignore_list: List of regular expression pattern applied to the full path.
        :param package_name: Name of the package to create.
        :param compression: Compression of the archive used by the python zipfile class.
        :type path: str
        :type output_path: str
        :type ignore_list: iterable
        :type package_name: str
        :type to_remove: iterable
        :type compression: constant
    """

    # Prepare ignore list
    if ignore_list is None:
        ignore_list = []
    regex_list = map(lambda e: re.compile(e), ignore_list)

    # Prepare package name
    if package_name is None:
        package_name = "%s.zip" % os.path.basename(path)
    package_name = os.path.normpath(package_name)

    # Prepare base path
    base_path = os.path.dirname(path)

    # Open archive for writing
    archive_path = os.path.join(output_path, package_name) if output_path is not None else package_name
    with zipfile.ZipFile(archive_path, 'w', compression=compression) as out:
        # Iterate on the source path
        for subdir, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(subdir, file)  # Relative path to the current working directory
                file_name = os.path.relpath(file_path, base_path) # Name in the archive

                # Filters
                if any(map(lambda r: r.search(file_path), regex_list)):
                    continue  # Skip file

                # Write file to archive
                out.write(file_path, file_name)

        # Add list of files to remove
        if to_remove is not None:
            out.writestr(helpers.TO_REMOVE_FILE, "\n".join(to_remove))


def apply_archive(in_path, out_path):
    """ Apply an update archive.

    :param in_path: Input archive path.
    :param out_path: Output directory path.
    :type in_path: str
    :type out_path: str
    """

    # Extract all files
    with zipfile.ZipFile(in_path) as archive:
        archive.extractall(out_path, filter(lambda n: n not in helpers.RESERVED_FILES, archive.namelist()))

        # Remove files
        try:
            to_remove = archive.read(helpers.TO_REMOVE_FILE).decode().split('\n')
            for n in to_remove:
                try:
                    os.remove('%s/%s' % (out_path, n))
                except FileNotFoundError:
                    pass  # File already removed
        except KeyError:  # No file to remove since no list is provided
            pass

