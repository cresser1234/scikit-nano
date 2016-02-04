#! /usr/bin/env python

from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import unittest

import nose
from nose.tools import assert_equal, assert_false, assert_true, \
    assert_is_instance
import numpy as np

from sknano.core.geometric_regions import Parallelepiped, Cuboid, Cube, \
    Ellipsoid, Sphere, Cylinder, Cone
from sknano.core.math import Point, Vector


class GeometricRegionsTestFixture(unittest.TestCase):

    @property
    def parallelepiped(self):
        return Parallelepiped()

    @property
    def cuboid(self):
        return Cuboid()

    @property
    def cube(self):
        return Cube()

    @property
    def ellipsoid(self):
        return Ellipsoid()

    @property
    def sphere(self):
        return Sphere()

    @property
    def cylinder(self):
        return Cylinder()

    @property
    def cone(self):
        return Cone()


def test_parallelepiped():
    r = Parallelepiped()
    assert_is_instance(r, Parallelepiped)
    assert_equal(r.o, Point([0, 0, 0]))
    assert_true(np.allclose(r.measure, 1.0))
    assert_equal(r.centroid, Point([1, 1, 0.5]))
    assert_true(r.contains([0.5, 0.5, 0.5]))
    assert_false(r.contains([0, 0, 1]))
    assert_is_instance(r.centroid, Point)


def test_cuboid():
    r = Cuboid()
    assert_is_instance(r, Cuboid)
    assert_equal(r.centroid, Point([0.5, 0.5, 0.5]))
    assert_true(np.allclose(r.measure, 1.0))
    assert_true(r.contains(r.centroid))
    assert_false(r.contains([-0.1, 0, 0]))
    assert_is_instance(r.centroid, Point)

    pmin = [-10, -10, -10]
    pmax = [10, 10, 10]
    r = Cuboid(pmin=pmin, pmax=pmax)
    assert_true(np.allclose(r.pmin, pmin))
    assert_true(np.allclose(r.pmax, pmax))

    pmin = [5, 5, 5]
    pmax = [10, 10, 10]
    r = Cuboid(pmin=pmin, pmax=pmax)
    assert_true(np.allclose(r.pmin, pmin))
    assert_true(np.allclose(r.pmax, pmax))

    pmin = [-10, -10, -10]
    pmax = [-5, -5, -5]
    r = Cuboid(pmin=pmin, pmax=pmax)
    assert_true(np.allclose(r.pmin, pmin))
    assert_true(np.allclose(r.pmax, pmax))


def test_cube():
    r = Cube()
    assert_is_instance(r, Cube)
    assert_equal(r.centroid, Point([0, 0, 0]))
    assert_true(np.allclose(r.measure, 1.0))
    assert_true(r.contains([0, 0, 0]))
    assert_false(r.contains([1, 1, 1]))
    assert_is_instance(r.centroid, Point)


def test_ellipsoid():
    r = Ellipsoid()
    assert_is_instance(r, Ellipsoid)
    assert_equal(r.centroid, Point([0, 0, 0]))
    assert_true(np.allclose(r.measure, 4 / 3 * np.pi))
    assert_true(r.contains(r.centroid))
    assert_false(r.contains([1.01, 1.01, 1.01]))
    assert_is_instance(r.centroid, Point)


def test_sphere():
    r = Sphere()
    assert_is_instance(r, Sphere)
    assert_equal(r.center, Point([0, 0, 0]))
    assert_equal(r.r, 1.0)
    assert_true(np.allclose(r.measure, 4 / 3 * np.pi))
    assert_true(r.contains([0, 0, 0]))
    assert_false(r.contains([1.1, 1.1, 1.1]))
    assert_is_instance(r.centroid, Point)


def test_cylinder():
    r = Cylinder()
    assert_is_instance(r, Cylinder)
    assert_true(np.allclose(r.measure, 2 * np.pi))
    assert_equal(r.p1, Point([0, 0, -1]))
    assert_equal(r.p2, Point([0, 0, 1]))
    assert_true(r.contains([0, 0, 0]))
    assert_false(r.contains([1.1, 0, 0]))
    assert_equal(r.centroid, Point())
    r.p2 = [0, 0, 2]
    assert_equal(r.centroid, Point([0, 0, 0.5]))
    assert_is_instance(r.centroid, Point)
    assert_is_instance(r.axis, Vector)


def test_cone():
    r = Cone()
    assert_is_instance(r, Cone)
    assert_true(np.allclose(r.measure, 2 * np.pi / 3))
    assert_equal(r.p1, Point(np.zeros(3)))
    assert_equal(r.p2, Point([0, 0, 2]))
    assert_true(r.contains([0, 0, 1]))
    assert_false(r.contains([0, 0, 2.1]))
    assert_is_instance(r.centroid, Point)
    assert_is_instance(r.axis, Vector)


if __name__ == '__main__':
    nose.runmodule()
