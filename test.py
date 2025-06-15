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

    def test_color_options(self):
        out = sysmess.fancy_box("X", border_color="red")
        self.assertIn('\x1b[31m', out)
        self.assertIn('\x1b[0m', out)
        out2 = sysmess.fancy_box("Y", title="T", title_color="green")
        self.assertIn('\x1b[32m', out2)
        out3 = sysmess.fancy_box("Z", body_color="blue")
        self.assertIn('\x1b[34m', out3)
        with self.assertRaises(ValueError):
            sysmess.fancy_box("Z", border_color="invalid")
        # style parameter for rounded corners
        box = sysmess.fancy_box("X", style="round")
        lines = box.splitlines()
        self.assertTrue(lines[0].startswith('╭'))
        self.assertTrue(lines[-1].startswith('╰'))
        with self.assertRaises(ValueError):
            sysmess.fancy_box("X", style="invalid")

    def test_wrap_max_width(self):
        text = "one two three four five six seven eight nine ten"
        box = sysmess.fancy_box(text, wrap=True, max_width=20)
        lines = box.splitlines()
        self.assertTrue(all(len(l) <= 20 for l in lines))
        self.assertTrue(len(lines) > 5)

    def test_wrap_terminal(self):
        import shutil, os
        text = "one two three four five six seven eight nine ten"
        old = shutil.get_terminal_size
        shutil.get_terminal_size = lambda: os.terminal_size((20, 0))
        try:
            box = sysmess.fancy_box(text, wrap=True)
            lines = box.splitlines()
            self.assertTrue(all(len(l) <= 20 for l in lines))
        finally:
            shutil.get_terminal_size = old

if __name__ == '__main__':
    # Run tests in verbose mode to show each test name and status
    unittest.main(verbosity=2)