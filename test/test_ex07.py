import pytest


class TestEx07:

    @pytest.fixture
    def target(self):
        from my_ros2_examples_py.ex07 import Foo
        return Foo()

    def test_answer_9_plus_1(self, target):
        assert target.func(9) == 10
