from division import division


if division(10, 5) != 2:
    raise Exception('Деление не работает!!!')


if division(100, 25) != 4:
    raise Exception('Деление не работает!!!')


print('OK!!!')