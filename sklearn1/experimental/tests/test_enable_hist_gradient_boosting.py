"""Tests for making sure experimental imports work as expected."""

import textwrap

from sklearn1.utils._testing import assert_run_python_script


def test_imports_strategies():
    # Make sure different import strategies work or fail as expected.

    # Since Python caches the imported modules, we need to run a child process
    # for every test case. Else, the tests would not be independent
    # (manually removing the imports from the cache (sys.modules) is not
    # recommended and can lead to many complications).

    good_import = """
    from sklearn1.experimental import enable_hist_gradient_boosting
    from sklearn1.ensemble import GradientBoostingClassifier
    from sklearn1.ensemble import GradientBoostingRegressor
    """
    assert_run_python_script(textwrap.dedent(good_import))

    good_import_with_ensemble_first = """
    import sklearn1.ensemble
    from sklearn1.experimental import enable_hist_gradient_boosting
    from sklearn1.ensemble import GradientBoostingClassifier
    from sklearn1.ensemble import GradientBoostingRegressor
    """
    assert_run_python_script(textwrap.dedent(good_import_with_ensemble_first))

    bad_imports = """
    import pytest

    with pytest.raises(ImportError):
        from sklearn1.ensemble import HistGradientBoostingClassifier

    with pytest.raises(ImportError):
        from sklearn1.ensemble._hist_gradient_boosting import (
            HistGradientBoostingClassifier)

    import sklearn1.experimental
    with pytest.raises(ImportError):
        from sklearn1.ensemble import HistGradientBoostingClassifier
    """
    assert_run_python_script(textwrap.dedent(bad_imports))
