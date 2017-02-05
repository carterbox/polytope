#!/usr/bin/env python
"""Benchmarks for the polytope subpackage."""
import logging

import timeit
import numpy as np
import polytope as pc


log = logging.getLogger('polytope.polytope')
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def random_polytope(ndims=4):
    """Return a random polytope."""

    A = np.random.rand(ndims, ndims)
    b = np.random.rand(ndims)
    p = pc.Polytope(A, b)

    return p


def setup_translate(ndims=4):
    """Return random input parameters for _translate."""

    d = np.random.rand(ndims)
    p = random_polytope(ndims)

    return p, d


def bench_translate(reps=int(1e6)):
    """Time how long it takes to translate polytopes."""

    t = timeit.timeit("pc.polytope._translate(p, d)",
                      ("from __main__ import setup_translate\n" +
                       "import polytope as pc\n" +
                       "p, d = setup_translate()"),
                      number=reps)

    log.info("%.3e Hz _translate", t/reps)
    return t


def setup_rotate1(ndims=4):
    """Return random input parameters for _rotate main rotations."""

    i, j = np.random.choice(ndims, 2, replace=False)
    theta = (np.random.rand(1) * 2 - 1) * np.pi
    p = random_polytope(ndims)

    return p, i, j, theta


def bench_rotate1(reps=int(1e6)):
    """Time how long it takes to rotate polytopes."""

    t = timeit.timeit("pc.polytope._rotate(p, i, j, theta=theta)",
                      ("from __main__ import setup_rotate1\n" +
                       "import polytope as pc\n" +
                       "p, i, j, theta = setup_rotate1()"),
                      number=reps)

    log.info("%.3e Hz _rotate", t/reps)
    return t


def bench_is_empty(reps=int(1e6)):
    """Time how long it takes to check if a polytope is empty."""

    t = timeit.timeit("pc.polytope.is_empty(p)",
                      ("from __main__ import random_polytope\n" +
                       "import polytope as pc\n" +
                       "p = random_polytope()"),
                      number=reps)

    log.info("%.3e Hz is_empty", t/reps)
    return t


def bench_cheby_ball(reps=int(1e6)):
    """Time how long it takes find the radius and center."""

    t = timeit.timeit("pc.polytope.cheby_ball(p)",
                      ("from __main__ import random_polytope\n" +
                       "import polytope as pc\n" +
                       "p = random_polytope()"),
                      number=reps)

    log.info("%.3e Hz cheby_ball", t/reps)
    return t


def bench_bounding_box(reps=int(1e6)):
    """Time how long it takes to calculate the bounding box."""

    t = timeit.timeit("pc.polytope.bounding_box(p)",
                      ("from __main__ import random_polytope\n" +
                       "import polytope as pc\n" +
                       "p = random_polytope()"),
                      number=reps)

    log.info("%.3e Hz bounding_box", t/reps)
    return t


if __name__ == '__main__':
    bench_bounding_box(1000)
    bench_cheby_ball(1000)
    bench_is_empty(1000)
    bench_rotate1(1000)
    bench_translate(1000)
