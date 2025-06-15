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

    # Colored example
    print(sysmess.fancy_box(
        "This box has colored border, title, and body.",
        title="Colored",
        border_color="magenta",
        title_color="cyan",
        body_color="green",
        bold=True
    ))

    # Rounded corners
    print(sysmess.fancy_box(
        "Rounded corners!",
        title="Round",
        style="round"
    ))

    # Show measured width
    width = sysmess.measure_box_width(multiline, title="Multi-line")
    print(f"Measured box width: {width}")

    # Wrapping example
    long_text = """
    monkey violin curtain purple dragonfly river carpet candle sandwich turtle notebook ice cream basket sweater 
    sunflower chair pepper ladder apple window ocean blanket piano feather pillow cloud donkey bicycle pepperoni 
    jacket forest mirror jellyfish hammock orange table pineapple brush flamingo book sweater umbrella hamburger 
    mountain suitcase elevator kiwi telephone lantern rabbit cookie clock wheel zebra printer grapes turtle planet 
    sweater basket bee flower sandwich lamp
    here is a much longer list of random text without punctuation or capitals
    giraffe mitten lamp cornfield river stone banana notebook galaxy sunflower velvet blanket swing computer dolphin moonlight puzzle chair velvet guitar chocolate broomstick lantern velvet ocean starfish bottle paper forest pillow lemonade mirror mushroom pencil mountain apple jacket rabbit window carrot feather cereal planet biscuit jellyfish turtle book rocket playground zipper sweater pillow acorn sandwich peach painting tulip butterfly highway ladder mango rainbow elephant flower dragonfly suitcase robot thumbtack zipper castle lamp button peanut tornado bicycle river polka dot marmalade suitcase doormat emerald locket television violin cupcake sandbox whisker cricket tornado orange marble pumpkin dresser velvet marshmallow dragonfly cabinet rose lotion blanket pillow slipper jacket acorn happy rainbow feather breeze apple zebra lamp mountain balloon pillow frog cupcake suitcase pitcher sweater ceiling button radio velvet marshmallow popcorn drawer planet planet acorn sweater starfish bicycle
"""
    print(sysmess.fancy_box(long_text, wrap=True, max_width=60))

if __name__ == "__main__":
    main()