# -*- coding: utf-8 -*-
""" Test for the core. """

import unittest
import os
import zipfile
import shutil

import updater


class TestCore(unittest.TestCase):
    """ Unit-tests for the core. """

    def setUp(self):
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Set the working directory to the root.

    def test_create_archive(self):
        """ Test basic archive creation. """
        out_name = 'tests/in.zip'
        updater.create_archive("tests/in", ignore_list=updater.COMMON_FILTERS, package_name=out_name)

        # Check
        self.assertTrue(os.path.isfile(out_name))
        with zipfile.ZipFile(out_name, 'r') as archive:
            self.assertEqual(len(archive.filelist), 5)

        # Clean
        os.remove(out_name)

    def test_apply_archive(self):
        """ Test archive decompression. """
        out_name = 'tests/in.zip'
        updater.create_archive("tests/in", ignore_list=updater.COMMON_FILTERS, package_name=out_name,
                               to_remove=['in/C.txt', 'in/B.txt', 'in/not_here'])

        out_path = 'tests/out'
        shutil.rmtree(out_path, ignore_errors=True)
        updater.apply_archive(out_name, out_path)

        # Check
        self.assertTrue(os.path.isfile('%s/in/A.txt' % out_path))
        self.assertTrue(os.path.isfile('%s/in/sub/D.txt' % out_path))
        self.assertFalse(os.path.isfile('%s/in/B.txt' % out_path))
        self.assertFalse(os.path.isfile('%s/in/C.txt' % out_path))

        # Clean
        os.remove(out_name)
        shutil.rmtree(out_path, ignore_errors=True)
