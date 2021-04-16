#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'limin'

import os

def func(x):
    return x +1

@pytest.mark.flaky(reruns=5)
def test_answer():
    assert func(3)==4