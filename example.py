#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" An example of using the `ProgressPool`

@author  Valentin Haenel <valentin.haenel@epfl.ch>

"""

import time
import random
from multiprocessing import Pool
from progresspool import ProgressPool

def f(x):
    time.sleep(random.uniform(0,3))
    return x*x

if __name__ == '__main__':
    print "Using a normal pool... you never know when it is done..."
    p = Pool()
    p.map(f, range(100))
    print "Oh... finally... it has completed...\n"

    time.sleep(3)

    print "Now using a progress pool... enjoy the ride! :D"
    pp = ProgressPool()
    pp.map(f, range(100))
