# -*- coding: utf-8 -*-
"""
===============================================================================
Atom classes for crystal lattices (:mod:`sknano.core.atoms._lattice_atoms`)
===============================================================================

.. currentmodule:: sknano.core.atoms._lattice_atoms

"""
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals
__docformat__ = 'restructuredtext en'

# from operator import attrgetter
from functools import total_ordering
import copy
import numbers
import numpy as np

from sknano.core.math import Vector

from ._atoms import Atom, Atoms

__all__ = ['LatticeAtom', 'LatticeAtoms']


@total_ordering
class LatticeAtom(Atom):
    """An abstract object representation of a crystal structure lattice atom.

    Parameters
    ----------
    lattice : :class:`~sknano.core.crystallography.Crystal3DLattice`
    xs, ys, zs : float
    """

    def __init__(self, *args, lattice=None, xs=None, ys=None, zs=None,
                 **kwargs):

        super().__init__(*args, **kwargs)

        self.lattice = lattice
        try:
            self.rs = Vector([xs, ys, zs])
        except AttributeError:
            pass

        self.fmtstr = super().fmtstr + \
            ", lattice={lattice!r}, xs={xs:.6f}, ys={ys:.6f}, zs={zs:.6f}"

    def __eq__(self, other):
        return self.rs == other.rs and super().__eq__(other)

    def __lt__(self, other):
        """Test if `self` is *less than* `other`."""
        return (self.rs < other.rs and super().__le__(other)) or \
            (self.rs <= other.rs and super().__lt__(other))

    def __dir__(self):
        attrs = super().__dir__()
        attrs.extend(['lattice', 'xs', 'ys', 'zs'])
        return attrs

    @property
    def xs(self):
        """:math:`x`-coordinate in units of **Angstroms**.

        Returns
        -------
        float
            :math:`x`-coordinate in units of **Angstroms**.

        """
        return self.rs.x

    @xs.setter
    def xs(self, value):
        """Set `Atom` :math:`x`-coordinate in units of **Angstroms**.

        Parameters
        ----------
        value : float
            :math:`x`-coordinate in units of **Angstroms**.

        """
        if not isinstance(value, numbers.Number):
            raise TypeError('Expected a number')
        rs = self.rs
        rs.x = value
        self._update_cartesian_coordinate(rs)

    @property
    def ys(self):
        """:math:`y`-coordinate in units of **Angstroms**.

        Returns
        -------
        float
            :math:`y`-coordinate in units of **Angstroms**.

        """
        return self.rs.y

    @ys.setter
    def ys(self, value):
        """Set `Atom` :math:`y`-coordinate in units of **Angstroms**.

        Parameters
        ----------
        value : float
            :math:`y`-coordinate in units of **Angstroms**.

        """
        if not isinstance(value, numbers.Number):
            raise TypeError('Expected a number')
        rs = self.rs
        rs.y = value
        self._update_cartesian_coordinate(rs)

    @property
    def zs(self):
        """:math:`z`-coordinate in units of **Angstroms**.

        Returns
        -------
        float
            :math:`z`-coordinate in units of **Angstroms**.

        """
        return self.rs.z

    @zs.setter
    def zs(self, value):
        """Set `Atom` :math:`z`-coordinate in units of **Angstroms**.

        Parameters
        ----------
        value : float
            :math:`z`-coordinate in units of **Angstroms**.

        """
        if not isinstance(value, numbers.Number):
            raise TypeError('Expected a number')
        rs = self.rs
        rs.z = value
        self._update_cartesian_coordinate(rs)

    @property
    def rs(self):
        """:math:`x, y, z` components of `Atom` position vector.

        Returns
        -------
        ndarray
            3-element ndarray of [:math:`x, y, z`] coordinates of `Atom`.

        """
        try:
            return Vector(self.lattice.cartesian_to_fractional(self.r))
        except AttributeError:
            return Vector()

    @rs.setter
    def rs(self, value):
        """Set :math:`x, y, z` components of `Atom` position vector.

        Parameters
        ----------
        value : array_like
            :math:`x, y, z` coordinates of `Atom` position vector relative to
            the origin.

        """
        if not isinstance(value, (list, np.ndarray)):
            raise TypeError('Expected an array_like object')
        rs = Vector(value, nd=3)
        self._update_cartesian_coordinate(rs)

    def _update_cartesian_coordinate(self, rs):
        self.r = Vector(self.lattice.fractional_to_cartesian(rs))

    @property
    def lattice(self):
        """:class:`~sknano.core.crystallography.Crystal3DLattice`."""
        return self._lattice

    @lattice.setter
    def lattice(self, value):
        self._lattice = copy.copy(value)

    def rotate(self, **kwargs):
        """Rotate `Atom` position vector.

        Parameters
        ----------
        angle : float
        axis : :class:`~sknano.core.math.Vector`, optional
        anchor_point : :class:`~sknano.core.math.Point`, optional
        rot_point : :class:`~sknano.core.math.Point`, optional
        from_vector, to_vector : :class:`~sknano.core.math.Vector`, optional
        degrees : bool, optional
        transform_matrix : :class:`~numpy:numpy.ndarray`

        """
        try:
            self.lattice.rotate(**kwargs)
        except AttributeError:
            pass
        super().rotate(**kwargs)

    def translate(self, t, fix_anchor_point=True):
        """Translate `Atom` position vector by :class:`Vector` `t`.

        Parameters
        ----------
        t : :class:`Vector`
        fix_anchor_point : bool, optional

        """
        # TODO compare timing benchmarks for translation of position vector.
        try:
            self.lattice.translate(t, fix_anchor_point=fix_anchor_point)
        except AttributeError:
            pass
        super().translate(t, fix_anchor_point=fix_anchor_point)

    def todict(self):
        super_dict = super().todict()
        super_dict.update(dict(lattice=self.lattice, xs=self.xs, ys=self.ys,
                               zs=self.zs))
        return super_dict


class LatticeAtoms(Atoms):
    """An `Atoms` sub-class for crystal structure lattice atoms.

    Sub-class of `Atoms` class, and a container class for lists of
    :class:`~sknano.core.atoms.LatticeAtom` instances.

    Parameters
    ----------
    atoms : {None, sequence, `LatticeAtoms`}, optional
        if not `None`, then a list of `LatticeAtom` instance objects or an
        existing `LatticeAtoms` instance object.

    """

    @property
    def __atom_class__(self):
        return LatticeAtom

    @property
    def rs(self):
        """:class:`~numpy:numpy.ndarray` of :attr:`Atom.r` position \
            `Vector`\ s"""
        return np.asarray([atom.rs for atom in self])

    @property
    def xs(self):
        """:class:`~numpy:numpy.ndarray` of `Atom`\ s :math:`x` coordinates."""
        return self.rs[:, 0]

    @property
    def ys(self):
        """:class:`~numpy:numpy.ndarray` of `Atom`\ s :math:`y` coordinates."""
        return self.rs[:, 1]

    @property
    def zs(self):
        """:class:`~numpy:numpy.ndarray` of `Atom`\ s :math:`z` coordinates."""
        return self.rs[:, 2]

    @property
    def lattice(self):
        try:
            return self[0].lattice
        except IndexError:
            return None

    @lattice.setter
    def lattice(self, value):
        [setattr(atom, 'lattice', value) for atom in self]