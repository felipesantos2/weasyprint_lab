# pytest doc
# https://docs.pytest.org/en/stable/index.html
#
# ARRANGE
# SUT
# 	não podemos ter um input e output verdadeiro, temos que mocar essas informações ou simular elas de alguma forma
# ASSERT


def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5
