def is_Kaukas(region):
    Kaukas = ["Чечня", "Дагестан", "Северная-Осетия", "Ставропольский Край", "Адыгея"]
    if region in Kaukas:
        return 'Да, это СКФО'
    else:
        return 'Нет, данный регион не относится к СКФО'


