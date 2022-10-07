import re
from typing import List, Any


def filter_query(param: str, data: List[str]) -> List[str]:
    return list(filter(lambda l: param in l, data))


def filter_not_query(param: str, data: List[str]) -> List[str]:
    return list(filter(lambda l: param not in l, data))


def filter_or_query(param: str, data: List[str]) -> List[str]:
    return list(filter((lambda l: any(a in l for a in param.split(' '))), data))


def filter_and_query(param: str, data: List[str]) -> List[str]:
    return list(filter((lambda l: all(a in l for a in param.split(' '))), data))


def map_query(param: str, data: List[str]) -> List[str]:
    # return list(map(lambda l: l.split(' ')[int(param)], data))
    return list(map(lambda l: ' '.join(l.split(' ')[int(a)] for a in str(param).split(' ')), data))


def unique_query(data: List[str], *args: Any, **kwargs: Any) -> List[str]:
    return list(set(data))


def sort_query(param: str, data: List[str]) -> List[str]:
    return sorted(data, reverse=(param == 'desc'))


def limit_query(param: str, data: List[str]) -> List[str]:
    return data[:int(param)]


def regex_query(param: str, data: List[str]) -> List[str]:
    qre = re.compile(param)
    return list(filter(lambda l: qre.search(l), data))


# here be tests

if __name__ == '__main__':
    print(filter_query('42', ['123 42 566 JSHDJ ADD', 'ewhjkdwq 43242 dhjdjsahd']))
    print(map_query('1', ['1 2 3 4 5', '55 44 33']))
    print(unique_query(['123', '123', '234']))
    print(sort_query('desc', ['123', '873', '023']))
    print(limit_query('2', ['43', '22', '66', '092']))
    # print(sort_query('desc', '342432d sajkas djk'))

    print(filter_not_query('123', ['123 42 566 JSHDJ ADD', 'ewhjkdwq 43242 dhjdjsahd']))
    print(filter_or_query('ZYZZY ADD 42', ['123 42 566 JSHDJ ADD', 'ewhjkdwq 43242 dhjdjsahd']))
    print(filter_and_query('ADD 42', ['123 42 566 JSHDJ ADD', 'ewhjkdwq 43242 dhjdjsahd']))

    print(regex_query('566', ['123 42 566 JSHDJ ADD', 'ewhjkdwq 43242 dhjdjsahd']))
