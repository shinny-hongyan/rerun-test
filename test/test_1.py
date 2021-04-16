#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'limin'

import os
import pytest
from datetime import datetime

def func(x):
    return x +1

@pytest.mark.flaky(reruns=20, reruns_delay=1)
def test_answer():
    now = datetime.now()
    dt_string = now.strftime("%S")
    assert (int)(dt_string) % 10 == 0