#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TNTdiff - The Namelist Tool: a namelist comparator.
"""

from __future__ import print_function, absolute_import, unicode_literals, division

import os
import sys

# Automatically set the python path
sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'src')
)

from thenamelisttool.entrypoints import tntdiff as tnt_cli


if __name__ == '__main__':
    tnt_cli.main()
