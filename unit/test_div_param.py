import pytest

from unit.div import div


@pytest.mark.happy
@pytest.mark.parametrize("num1, num2, exception_num", {
    (10, 2, 5),
    (12, 3, 4),
    (1000000, 1, 1000000)
})
def test_div_int_param(num1, num2, exception_num):
    assert div(num1, num2) == exception_num


@pytest.mark.exception
@pytest.mark.parametrize("num1, num2, exception_num", {
    (12, 5, 2.4),
    (12.3, 0.2, 61.5),
    (10.2, 0.2, 51),
    (11, 0.2, 55),
    (13.1, 2, 6.55),
    (10, 3, 3.333333)
})
def test_div_float(num1, num2, exception_num):
    assert div(num1, num2) == exception_num


@pytest.mark.exception
@pytest.mark.parametrize("num1, num2", {
    (10, 'a'),
    ('abc', 10),
    ('bbb', 'ccc')
})
def test_div_exception(num1, num2):
    assert div(num1, num2)


@pytest.mark.exception
@pytest.mark.parametrize("num1", {
    10,
    40
})
def test_div_zero(num1):
    assert div(num1, 0) is None
