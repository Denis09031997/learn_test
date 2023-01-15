from Kaukas import is_Kaukas


def test_is_Kaukas():
    assert is_Kaukas('Дагестан') == 'Да, это СКФО'


def test_is_Kaukas():
    assert is_Kaukas('Краснодарский Край') == 'Нет, данный регион не относится к СКФО'