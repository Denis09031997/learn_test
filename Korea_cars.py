def is_Korea_car(l):
    Korea = ['KIA', 'Hyandai', 'Genesis']
    result = []
    for i in l:
        if i in Korea:
            result.append(i)

    return result

