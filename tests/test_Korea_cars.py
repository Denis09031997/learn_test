from Korea_cars import is_Korea_car


assert is_Korea_car(['KIA', 'LADA', 'Genesis', 'MAZDA', 'Opel']) == ['KIA', 'Genesis']
assert is_Korea_car(['Lada', 'Volvo']) == []