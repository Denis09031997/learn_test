from cheaply import is_cheaply


def test_is_cheaply():
    assert is_cheaply('Сбербанк') == 'Да, этот банк дешевый' # У этого банка высокие % ставки


def test_is_cheaply():
    assert is_cheaply("Киви") == 'Да, этот банк дешевый'


def test_is_cheaply():
    assert is_cheaply('Абсолют') == 'У этого банка высокие % ставки'