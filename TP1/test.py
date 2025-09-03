import pytest
import fonctions as f

def test_puissance_positive():
    assert f.puissance(2, 3) == 8
    assert f.puissance(0, 5) == 0
    assert f.puissance(5, 0) == 1

def test_2():
    assert f.puissance(-2,-1)==-0.5

def test_puissance_erreur_type():
    with pytest.raises(ValueError):
        f.puissance(0,0)
