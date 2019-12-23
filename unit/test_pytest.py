import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


def set_module():
    print("setup module")


def setup_function():
    print("setup function")


class TestClass:
    def setup(self):
        print("setup")

    @classmethod
    def setup_class(cls):
        print("setup class")

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "checkr")
