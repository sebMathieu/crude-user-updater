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
        updater.create_archive("tests/in", ignore_list=updater.COMMON_FILTERS + ['no.+'], package_name=out_name)

        # Check
        self.assertTrue(os.path.isfile(out_name))
        with zipfile.ZipFile(out_name, 'r') as archive:
            self.assertEqual(len(archive.filelist), 6)

        # Clean
        os.remove(out_name)

    def test_apply_archive(self):
        """ Test archive decompression. """
        out_name = 'tests/in.zip'
        updater.create_archive("tests/in", ignore_list=updater.COMMON_FILTERS, package_name=out_name,
                               to_remove=['in/C.txt', 'in/B.txt', 'in/not_here'])

        # Prepare out path
        out_path = 'tests/out'
        shutil.rmtree(out_path, ignore_errors=True)
        os.makedirs("tests/out", exist_ok=True)
        with open('tests/out/to_backup', 'w') as f:
            f.write("To backup !")

        # Apply
        updater.apply_archive(out_name, out_path, 'tests')

        # Check
        self.assertTrue(os.path.isfile('%s/in/A.txt' % out_path))
        self.assertTrue(os.path.isfile('%s/in/sub/D.txt' % out_path))
        self.assertFalse(os.path.isfile('%s/in/B.txt' % out_path))
        self.assertFalse(os.path.isfile('%s/in/C.txt' % out_path))

        # Check backup
        backup_path = 'tests/backup.zip'
        self.assertTrue(os.path.isfile(backup_path))
        with zipfile.ZipFile(backup_path) as f:
            self.assertIn("out/to_backup", f.namelist())

        # Clean
        os.remove(out_name)
        os.remove(backup_path)
        shutil.rmtree(out_path, ignore_errors=True)
