# tests/test_alg.py

import pytest
from alg import process_input

def run(input_str):
    # helper: нормализует переводы строк в конце
    return process_input(input_str).rstrip()

def test_simple_chain():
    inp = "3 2\n1 2\n2 3\n"
    # весь граф связный, поэтому компонент {1,2,3}
    assert run(inp) == "3\n1 2 3"

def test_two_components():
    inp = "4 2\n1 2\n3 4\n"
    # из 1 достижима только {1,2}
    assert run(inp) == "2\n1 2"

def test_loop_and_multiedge():
    inp = "3 4\n1 1\n2 3\n2 3\n1 2\n"
    # петля на 1, ребро 1-2, поэтому компонент {1,2}, вершина 3 не достижима
    assert run(inp) == "2\n1 2"

def test_isolated_vertex():
    inp = "5 0\n"
    # только одна вершина 1
    assert run(inp) == "1\n1"
