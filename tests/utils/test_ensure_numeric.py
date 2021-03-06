from math import inf, nan

import pytest
from hypothesis import given
from hypothesis.strategies import floats, integers

from pysoleng.utils import ensure_numeric


@pytest.mark.utils
@given(integers())
def test_integers(value):
    """Functional test to ensure the validate_datetime() method
    runs properly on integer values."""
    ensure_numeric(value, valid_types=[int])


@pytest.mark.utils
@given(floats(allow_nan=True, allow_infinity=True))
def test_floats(value):
    """Functional test to ensure the validate_datetime() method
    runs properly on float values."""
    ensure_numeric(
        value, valid_types=[float], nan_acceptable=True, inf_acceptable=True
    )


@pytest.mark.utils
def test_iterable():
    """Functional test to ensure the validate_datetime() method
    runs properly on iterables."""
    ensure_numeric(
        [1, 2, 3], valid_types=[int], nan_acceptable=True, inf_acceptable=True
    )
    ensure_numeric(
        [1.2, -2.4, 3.7, inf],
        valid_types=[float],
        nan_acceptable=True,
        inf_acceptable=True,
    )
    ensure_numeric(
        [1, 2.5, inf, nan],
        valid_types=[int, float],
        nan_acceptable=True,
        inf_acceptable=True,
    )


@pytest.mark.utils
def test_nan_inf():
    """Tests to ensure ensure_numeric() throws ValueErrors
    for NaN and infinite values when those parameters are
    set to `False`."""
    with pytest.raises(ValueError):
        # Test for NaN values
        assert ensure_numeric(
            nan, valid_types=[int, float], nan_acceptable=False
        )
    with pytest.raises(ValueError):
        # Test for infinite values
        assert ensure_numeric(
            inf, valid_types=[int, float], inf_acceptable=False
        )


@pytest.mark.utils
def test_invalid_types():
    """Tests to ensure ensure_numeric() throws TypeErrors
    for invalid types."""
    with pytest.raises(TypeError):
        # Test for strings
        assert ensure_numeric("blah", valid_types=[int, float])
