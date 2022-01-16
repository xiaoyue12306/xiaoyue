import pytest, math


# pytest参数化
@pytest.mark.parametrize(
    'base, exponent, expected',
    [(1, 1, 1),
     (2, 2, 4),
     (3, 3, 27)],
    ids=["case1","case2","case3"]
)
def test_pow(base, exponent, expected):
    assert math.pow(base, exponent) == expected


if __name__ == 'main':
    pytest.main()
