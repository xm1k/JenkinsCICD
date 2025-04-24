import pytest
from alg import process_input

def test_reverse_simple():
    assert process_input('hello') == 'olleh'
