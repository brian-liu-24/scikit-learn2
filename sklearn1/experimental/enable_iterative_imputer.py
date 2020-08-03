"""Enables IterativeImputer

The API and results of this estimator might change without any deprecation
cycle.

Importing this file dynamically sets :class:`~sklearn1.impute.IterativeImputer`
as an attribute of the impute module::

    >>> # explicitly require this experimental feature
    >>> from sklearn1.experimental import enable_iterative_imputer  # noqa
    >>> # now you can import normally from impute
    >>> from sklearn1.impute import IterativeImputer
"""

from ..impute._iterative import IterativeImputer
from .. import impute

# use settattr to avoid mypy errors when monkeypatching
setattr(impute, 'IterativeImputer', IterativeImputer)
impute.__all__ += ['IterativeImputer']
