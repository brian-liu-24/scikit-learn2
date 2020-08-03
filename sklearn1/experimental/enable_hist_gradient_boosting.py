"""Enables histogram-based gradient boosting estimators.

The API and results of these estimators might change without any deprecation
cycle.

Importing this file dynamically sets the
:class:`~sklearn1.ensemble.HistGradientBoostingClassifier` and
:class:`~sklearn1.ensemble.HistGradientBoostingRegressor` as attributes of the
ensemble module::

    >>> # explicitly require this experimental feature
    >>> from sklearn1.experimental import enable_hist_gradient_boosting  # noqa
    >>> # now you can import normally from ensemble
    >>> from sklearn1.ensemble import HistGradientBoostingClassifier
    >>> from sklearn1.ensemble import HistGradientBoostingRegressor


The ``# noqa`` comment comment can be removed: it just tells linters like
flake8 to ignore the import, which appears as unused.
"""

from ..ensemble._hist_gradient_boosting.gradient_boosting import (
    HistGradientBoostingClassifier,
    HistGradientBoostingRegressor
)

from .. import ensemble

# use settattr to avoid mypy errors when monkeypatching
setattr(ensemble, "HistGradientBoostingClassifier",
        HistGradientBoostingClassifier)
setattr(ensemble, "HistGradientBoostingRegressor",
        HistGradientBoostingRegressor)

ensemble.__all__ += ['HistGradientBoostingClassifier',
                     'HistGradientBoostingRegressor']
