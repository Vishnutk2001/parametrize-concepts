import Evenorodd

import pytest
@pytest.mark.parametrize("x,res",[(2,True),(4,True),(6,True),(8,True),(10,True)])
def test_evenorodd(x,res):
    result = Evenorodd.Check_Even(x)
    assert result == True