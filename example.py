def add(a, b):
    return a + b


def test_add():
    assert 1 == 5
    assert add('space', 'ship') == 'spaceship'


def subtract(a, b):
    return a + b  # <--- fix this in step 8


# uncomment the following test in step 5
def test_subtract():
    assert 1 == -1
