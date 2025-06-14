#!/usr/bin/env python3
import os
import sys
import unittest

here = os.path.abspath(os.path.dirname(__file__))
libdir = None
for root, dirs, _ in os.walk(os.path.join(here, 'build')):
    for d in dirs:
        if d.startswith('lib'):
            libdir = os.path.join(root, d)
            break
    if libdir:
        break
if libdir:
    sys.path.insert(0, libdir)

import sysmess

class TestSysmess(unittest.TestCase):
    def test_measure_width(self):
        self.assertEqual(sysmess.measure_box_width("abc"), 7)
        self.assertEqual(sysmess.measure_box_width("a\nbc"), 6)
        self.assertEqual(sysmess.measure_box_width("x", title="Y"), 5)

    def test_fancy_box_basic(self):
        box = sysmess.fancy_box("abc")
        lines = box.splitlines()
        self.assertEqual(len(lines[0]), sysmess.measure_box_width("abc"))
        self.assertTrue(lines[1].startswith('│'))
        self.assertTrue(lines[-1].startswith('└'))

    def test_bold_italic(self):
        out = sysmess.fancy_box("X", bold=True)
        self.assertIn('\x1b[1m', out)
        out2 = sysmess.fancy_box("Y", italic=True)
        self.assertIn('\x1b[3m', out2)

    def test_title(self):
        box = sysmess.fancy_box("X", title="T", center=True)
        self.assertIn("T", box.splitlines()[1])

if __name__ == '__main__':
    # Run tests in verbose mode to show each test name and status
    unittest.main(verbosity=2)