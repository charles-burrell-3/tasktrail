from tasktrail.temp import temp


def test_temp():
    assert temp('this') == 'this'
