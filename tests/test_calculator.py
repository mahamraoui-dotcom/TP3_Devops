import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

from calculator import addition, multiplication

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0

def test_multiplication():
    assert multiplication(3, 4) == 12
    assert multiplication(5, 0) == 0