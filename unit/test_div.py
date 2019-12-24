import pytest

from unit.div import div


def test_div1():
    m = 4
    y = div(12, 3)
    assert y == m


"""
   课间作业订正，老师示例
"""


@pytest.mark.happy
@pytest.mark.parametrize("num1, num2, exception_num", {
    (10, 2, 5),
    (12, 3, 4),
    (1000000, 1, 1000000)
})
@pytest.mark.happy
def test_div_int_param(num1, num2, exception_num):
    assert div(num1, num2) == exception_num


@pytest.mark.happy
def test_div_int():
    assert div(10, 2) == 5
    assert div(12, 3) == 4
    assert div(100000000, 1) == 100000000


@pytest.mark.exception
def test_div_float():
    assert div(12, 5) == 2.4
    assert div(12.3, 0.2) == 61.5
    assert div(10.2, 0.2) == 51
    assert div(10, 3) == 3.333333333


@pytest.mark.exception
def test_div_exception():
    assert div(10, 'a')
    assert div('abc', 10)


@pytest.mark.exception
def test_div_zero():
    assert div(12, 0) is None
