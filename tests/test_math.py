import pytest
from pu import math


class TestAdd:
    def test_both_positive(self: "TestAdd") -> None:
        a = 2
        b = 2
        expected = 4
        assert math.add(a, b) == expected

    def test_a_positive_b_negative(self: "TestAdd") -> None:
        a = 1
        b = -1
        expected = 0
        assert math.add(a, b) == expected
    def test_a_negative_b_positive(self: "TestAdd") -> None:
        a = -1
        b = 1
        expected = 0
        assert math.add(a, b) == expected

    def test_both_negative(self: "TestAdd") -> None:
        a = -1
        b = -1
        expected = -2
        assert math.add(a, b) == expected

    def test_a_0_b_positive(self: "TestAdd") -> None:
        a = 0
        b = 1
        expected = 1
        assert math.add(a, b) == expected

    def test_a_0_b_negative(self: "TestAdd") -> None:
        a = 0
        b = -1
        expected = -1
        assert math.add(a, b) == expected

    def test_a_positive_b_0(self: "TestAdd") -> None:
        a = 1
        b = 0
        expected = 1
        assert math.add(a, b) == expected

    def test_a_negative_b_0(self: "TestAdd") -> None:
        a = -1
        b = 0
        expected = -1
        assert math.add(a, b) == expected

    def test_both_0(self: "TestAdd") -> None:
        a = 0
        b = 0
        expected = 0
        assert math.add(a, b) == expected



class TestSubtract:
    def test_both_positive(self: "TestSubtract") -> None:
        a = 1
        b = 1
        expected = 0
        assert math.subtract(a, b) == expected

    def test_a_positive_b_negative(self: "TestSubtract") -> None:
        a = 1
        b = -1
        expected = 2
        assert math.subtract(a, b) == expected

    def test_a_negative_b_positive(self: "TestSubtract") -> None:
        a = -1
        b = 1
        expected = -2
        assert math.subtract(a, b) == expected

    def test_both_negative(self: "TestSubtract") -> None:
        a = -1
        b = -1
        expected = 0
        assert math.subtract(a, b) == expected

    def test_a_0_b_positive(self: "TestSubtract") -> None:
        a = 0
        b = 1
        expected = -1
        assert math.subtract(a, b) == expected

    def test_a_0_b_negative(self: "TestSubtract") -> None:
        a = 0
        b = -1
        expected = 1
        assert math.subtract(a, b) == expected

    def test_a_positive_b_0(self: "TestSubtract") -> None:
        a = 1
        b = 0
        expected = 1
        assert math.subtract(a, b) == expected

    def test_a_negative_b_0(self: "TestSubtract") -> None:
        a = -1
        b = 0
        expected = -1
        assert math.subtract(a, b) == expected

    def test_both_0(self: "TestSubtract") -> None:
        a = 0
        b = 0
        expected = 0
        assert math.subtract(a, b) == expected



class TestMultiply:
    def test_both_positive(self: "TestMultiply") -> None:
        a = 2
        b = 3
        expected = 6
        assert math.multiply(a, b) == expected

    def test_a_positive_b_negative(self: "TestMultiply") -> None:
        a = 2
        b = -3
        expected = -6
        assert math.multiply(a, b) == expected

    def test_a_negative_b_positive(self: "TestMultiply") -> None:
        a = -2
        b = 3
        expected = -6
        assert math.multiply(a, b) == expected

    def test_both_negative(self: "TestMultiply") -> None:
        a = -2
        b = -3
        expected = 6
        assert math.multiply(a, b) == expected

    def test_a_0_b_positive(self: "TestMultiply") -> None:
        a = 0
        b = 3
        expected = 0
        assert math.multiply(a, b) == expected

    def test_a_0_b_negative(self: "TestMultiply") -> None:
        a = 0
        b = -3
        expected = 0
        assert math.multiply(a, b) == expected

    def test_a_positive_b_0(self: "TestMultiply") -> None:
        a = 2
        b = 0
        expected = 0
        assert math.multiply(a, b) == expected

    def test_a_negative_b_0(self: "TestMultiply") -> None:
        a = -2
        b = 0
        expected = 0
        assert math.multiply(a, b) == expected

    def test_both_0(self: "TestMultiply") -> None:
        a = 0
        b = 0
        expected = 0
        assert math.multiply(a, b) == expected

    def test_a_1_b_positive(self: "TestMultiply") -> None:
        a = 1
        b = 3
        assert math.multiply(a, b) == b

    def test_a_1_b_negative(self: "TestMultiply") -> None:
        a = 1
        b = -3
        assert math.multiply(a, b) == b

    def test_a_positive_b_1(self: "TestMultiply") -> None:
        a = 2
        b = 1
        assert math.multiply(a, b) == a

    def test_a_negative_b_1(self: "TestMultiply") -> None:
        a = -2
        b = 1
        assert math.multiply(a, b) == a



class TestDivide:
    def test_both_positive(self: "TestDivide") -> None:
        a = 2
        b = 2
        expected = 1.0
        assert math.divide(a, b) == expected

    def test_a_positive_b_negative(self: "TestDivide") -> None:
        a = 2
        b = -2
        expected = -1.0
        assert math.divide(a, b) == expected

    def test_a_negative_b_positive(self: "TestDivide") -> None:
        a = -2
        b = 2
        expected = -1.0
        assert math.divide(a, b) == expected

    def test_both_negative(self: "TestDivide") -> None:
        a = -2
        b = -2
        expected = 1.0
        assert math.divide(a, b) == expected

    def test_a_0_b_positive(self: "TestDivide") -> None:
        a = 0
        b = 2
        expected = 0.0
        assert math.divide(a, b) == expected

    def test_a_0_b_negative(self: "TestDivide") -> None:
        a = 0
        b = -2
        expected = 0.0
        assert math.divide(a, b) == expected

    def test_a_positive_b_0(self: "TestDivide") -> None:
        a = 2
        b = 0
        with pytest.raises(ZeroDivisionError):
            math.divide(a, b)

    def test_a_negative_b_0(self: "TestDivide") -> None:
        a = 2
        b = 0
        with pytest.raises(ZeroDivisionError):
            math.divide(a, b)

    def test_both_0(self: "TestDivide") -> None:
        a = 0
        b = 0
        with pytest.raises(ZeroDivisionError):
            math.divide(a, b)



class TestSquareRoot:
    def test_positive(self: "TestSquareRoot") -> None:
        a = 4
        expected = 2
        assert math.sqrt(a) == expected

    def test_negative(self: "TestSquareRoot") -> None:
        a = -4
        with pytest.raises(ArithmeticError):
            math.sqrt(a)

    def test_zero(self: "TestSquareRoot") -> None:
        a = 0
        expected = 0
        assert math.sqrt(a) == expected


class TestDouble:
    def test_positive(self: "TestDouble") -> None:
        expected = 6
        a = 3
        assert math.double(a) == expected

    def test_negative(self: "TestDouble") -> None:
        expected = -6
        a = -3
        assert math.double(a) == expected

    def test_zero(self: "TestDouble") -> None:
        expected = 0
        a = 0
        assert math.double(a) == expected
