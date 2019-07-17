#!/usr/bin/python

"""
Notes:
  2 dicts
    # ! recipe -> key: ingredient; val: int
    # ! ingredients -> key: ingredient, val: int
  problem?
    return how many batches of a recipe can be made from the ingredients that are available
  thoughts?
    test sample data
"""

import math
import numpy as np


def recipe_batches(recipe, ingredients):
    r_vals = []
    i_vals = []

    for v in recipe.values():
        r_vals.append(v)
    for v in ingredients.values():
        i_vals.append(v)
    ratios = []
    for (i, item) in enumerate(r_vals):
        if len(r_vals) != len(i_vals):
            return 0
        else:
            ratios.append(i_vals[i] / item)
    j = 0
    while j < len(ratios):
        if ratios[j] < 1:
            return 0
        else:
            return (math.floor(min(ratios)))
        j += 1


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 200, 'butter': 50, 'flour': 51}
    ingredients = {'milk': 400, 'butter': 100, 'flour': 51}
    batches = recipe_batches(recipe, ingredients)
    print(f'{batches} batches can be made from the available ingredients: {ingredients}.')
