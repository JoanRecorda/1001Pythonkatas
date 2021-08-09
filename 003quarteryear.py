import math

def quarter_of(month):
    return (math.ceil(month / 3))

def test_answer():
    assert (quarter_of(2), 1)
    assert (quarter_of(3), 1)
    assert (quarter_of(4), 2)
    assert (quarter_of(6), 2)
    assert (quarter_of(8), 3)
    assert (quarter_of(9), 3)
    assert (quarter_of(11), 4)