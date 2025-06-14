#!/usr/bin/env python3
"""Demonstration of sysmess extension module usage."""

import os
import sys

# Ensure we load the built extension from build/lib* if not installed
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

def main():
    # Simple message
    print(sysmess.fancy_box("Hello, World!"))

    # With a title
    print(sysmess.fancy_box(
        "This is a sample message.",
        title="Example"
    ))

    # Centered and bold title/message
    print(sysmess.fancy_box(
        "Centered & Bold",
        title="Style",
        center=True,
        bold=True
    ))

    # Multi-line message, italic
    multiline = "Line 1\nLine 2\nLine 3"
    print(sysmess.fancy_box(
        multiline,
        title="Multi-line",
        italic=True
    ))

    # Show measured width
    width = sysmess.measure_box_width(multiline, title="Multi-line")
    print(f"Measured box width: {width}")

if __name__ == "__main__":
    main()