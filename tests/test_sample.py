#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import logging
import os
from pathlib import Path

import kanilog
import pytest
import stdlogging
from add_parent_path import add_parent_path

with add_parent_path():
    import pickling_decorator


class TestClass:
    @pickling_decorator.pickling()
    def foo(self):
        print("something")

def mmm():
    pass



def test_func():
    t = TestClass()
    __import__('pdb').set_trace()
    t.foo()


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    kanilog.setup_logger(
        logfile="/tmp/%s.log" % (os.path.basename(__file__)), level=logging.DEBUG
    )
    stdlogging.enable()

    pytest.main([__file__, "-k test_", "-s"])
