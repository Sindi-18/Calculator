import pytest
import operators as op


def test_true():
    assert op.multiply(5, 5) == 25
    assert op.multiply("5", 5) == 25
    assert op.multiply("3.5", 2) == 7.0
    assert op.divide(10,5) == 2
    assert op.divide("10",2) == 5
def test_false():
    with pytest.raises(ValueError):
        op.multiply("a", "b")
    with pytest.raises(TypeError):
        op.multiply([1, 2], 5)

    with pytest.raises(ValueError):
        op.divide("a","b")
        def verify_history(history, expected_operations):