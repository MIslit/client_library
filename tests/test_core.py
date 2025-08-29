from client_library import core

def test_add_numbers():
    assert core.add(2, 3) == 5

def test_add_with_negative():
    assert core.add(-1, 1) == 0
