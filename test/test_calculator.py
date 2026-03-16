import pytest
from app.calculator import addition,multiplication

def test_add():
    a = 14
    b = -2
    c = addition(a,b)
    assert c == (14-2)

def test_multiplication():
    a = 14
    b = -2
    c = multiplication(a,b)
    assert c == (14*-2)