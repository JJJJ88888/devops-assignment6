from calc import add, subtract


def test_add():
    assert add(2, 3) == 999  # 故意寫錯，觸發 CI 門禁阻擋！


def test_subtract():
    assert subtract(5, 2) == 3