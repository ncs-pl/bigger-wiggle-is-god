#!/usr/bin/env python
import os


counter = 0
incr = 1
max_counter = 25

while True:
    # counter is the amount of space printed before the text
    # to create the expected effect, we simply increment counter, then decrement it
    if counter > max_counter:
        incr = -1
        counter = max_counter - 1
    elif counter < 0:
        incr = 1
        counter = 0

    print(" " * counter + "bigger wiggle")
    os.system("paplay bip.ogg")

    counter += incr
