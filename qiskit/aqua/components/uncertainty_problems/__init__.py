# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Uncertainty Problems (:mod:`qiskit.aqua.components.uncertainty_problems`)
=========================================================================
Uncertainty Problems

.. currentmodule:: qiskit.aqua.components.uncertainty_problems

Uncertainty Problem Base Classes
================================
:class:`UncertaintyProblem` is the base class from which further
base classes for univariate and multivariate problems are
derived

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   UncertaintyProblem
   UnivariateProblem
   MultivariateProblem

Univariate Problems
===================

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

    UnivariatePiecewiseLinearObjective

"""

from .uncertainty_problem import UncertaintyProblem
from .multivariate_problem import MultivariateProblem
from .univariate_problem import UnivariateProblem
from .univariate_piecewise_linear_objective import UnivariatePiecewiseLinearObjective

__all__ = ['UncertaintyProblem',
           'MultivariateProblem',
           'UnivariateProblem',
           'UnivariatePiecewiseLinearObjective']
