"""
  The multi-objective Park function.
  -- kandasamy@cs.cmu.edu
"""

# You should have one of the following two in this file:
#   1. objectives: A list of functions, each of which corresponds to an objective.
#   2. A function called compute_objectives which returns the value of all objectives when
#      called as a list, and an integer called num_objectives which indicates the number
#      of objectives.

# pylint: disable=invalid-name

import numpy as np


def _get_01_coords(x):
  """ Returns the coordinates normalised to (0,1). """
  x1 = x[0][0]
  x2 = x[0][1]
  x3 = float(x[1]) / (194.0 - 103.0)
  x4 = x[2] - 10.0
  return [x1, x2, x3, x4]


def park1_euc(x):
  """ Computes the park1 function. """
  max_val = 25.5872304
  x1 = x[0]
  x2 = x[1]
  x3 = x[2]
  x4 = x[3]
  ret1 = (x1/2) * (np.sqrt(1 + (x2 + x3**2)*x4/(x1**2)) - 1)
  ret2 = (x1 + 3*x4) * np.exp(1 + np.sin(x3))
  return min(ret1 + ret2, max_val)

def park1(x):
  """ Computes park1. """
  return park1_euc(_get_01_coords(x))


def park2_euc(x):
  """ Comutes the park2 function """
  max_val = 5.925698
  x1 = x[0]
  x2 = x[1]
  x3 = x[2]
  x4 = x[3]
  ret = (2.0/3.0) * np.exp(x1 + x2) - x4*np.sin(x3) + x3
  return min(ret, max_val)

def park2(x):
  """ Computes park1. """
  return park1_euc(_get_01_coords(x))

# Option 1
objectives = [park1, park2]

# Option 2
# num_objectives = 2
# def compute_objectives(x):
#   """ Computes the objectives. """
#   return [park1(x), park2(x)]

