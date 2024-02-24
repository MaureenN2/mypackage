from mypackage import mymodule

def test_top_n():
    """
    make sure the top_n works correctly
    """
    assert mymodule.top_n([8,3,2,7,4], 3) == [8,7,4], "incorrect"
    assert mymodule.top_n([9,6,2,5,8], 4) == [9,8,6,5], "incorrect"
    assert mymodule.top_n([3,4,5,1],2) == [5,4], "incorrect"