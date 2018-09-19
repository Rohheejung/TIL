# -*- coding: utf-8 -*-
"""
command_line_args_test.py

명령행 인자 처리를 실험한다.
"""

import sys

print(sys.argv)
print(len(sys.argv))
print(sys.argv[0])

for arg in sys.argv:
    print(arg)

