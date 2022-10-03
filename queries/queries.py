def filter_query(param, data):
    return list(filter(lambda l: param in l, data))


def map_query(param, data):
    return list(map(lambda l: l.split(' ')[int(param)], data))


def unique_query(data, *args, **kwargs):
    return list(set(data))


def sort_query(param, data):
    return sorted(data, reverse=(param == 'desc'))


def limit_query(param, data):
    return data[:int(param)]


# here be tests

if __name__ == '__main__':
    print(filter_query('42', ['123 42 566 JSHDJ ADD', 'ewhjkdwq 43242 dhjdjsahd']))
    print(map_query('1', ['1 2 3 4 5', '55 44 33']))
    print(unique_query(['123', '123', '234']))
    print(sort_query('desc', ['123', '873', '023']))
    print(limit_query('2', ['43', '22', '66', '092']))
    print(sort_query('desc', '342432d sajkas djk'))
