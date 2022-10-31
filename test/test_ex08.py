import pytest


class TestEx08:

    @pytest.fixture
    def target(self):
        from my_ros2_examples_py.ex08 import FizzBuzz
        return FizzBuzz()

    test_data = [
        (1, '1'),
        (2, '2'),
        (3, 'fizz'),
        (4, '4'),
        (5, 'buzz'),
        (6, 'fizz'),
        (7, '7'),
        (8, '8'),
        (9, 'fizz'),
        (10, 'buzz'),
        (11, '11'),
        (12, 'fizz'),
        (13, '13'),
        (14, '14'),
        (15, 'fizzbuzz'),
    ]

    @pytest.mark.parametrize('x, expected', test_data)
    def test_x_converted_to(self, target, x, expected):
        assert target.convert(x) == expected
