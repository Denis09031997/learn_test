def is_cheaply(bank):
    cheaply_banks = ["Металлинвестбанк", "Киви", "Промсвязьбанк", "Реалист"]

    if bank in cheaply_banks:
        return 'Да, этот банк дешевый'
    else:
        return 'У этого банка высокие % ставки'


