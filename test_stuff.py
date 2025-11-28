import main

def test_func1():
    assert main.func1(3) == 9
    #x = 1/0
    #raise Exception("Deliberate Exception for testing")
    assert main.func1(-4) == 16
    assert main.func1(0) == 0
    #assert main.func1(20) == 5  # This will fail

def test_func2():
    assert main.func2("Testing") == "Testin"
    assert main.func2("A") == ""

def test_func2_more():
    assert main.func2("Testing") == "Testin"
    assert main.func2("A") == ""


def test_bad_func1():
    #assert main.func1(2) == 5  # This will fail
    pass