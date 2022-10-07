from collections import defaultdict
from typing import Optional, List, Tuple, Any, Dict

from queries.constants import QUERIES


def get_data(filename: str) -> Optional[List[str]]:
    try:
        with open('data/'+filename) as f:
            return list(map(lambda l: l.strip(), f))
    except FileNotFoundError:
        return None


def parse_request(req: Any) -> Tuple[Optional[str], Optional[list]]:
    """
    The task required a POST request to contain a dict of five items:
    cmd1, value1, cmd2, value2 and file_name.
    To make this thing more useful, this parser keeps reverse compatibility, but
    adds an option to include any number of cmdX-valueX pairs. Also, the numbers do not
    have to be consistent, thus a BASIC-like numeration is supported (10-20-40 etc.).
    :param req: a POST request as is (Any because request.get_json() returns Optional[Any])
    :return: (filename, a list of queries sorted according to their Xs). Any None results in an error.
    """

    try:
        fname: str = req.pop('file_name')
    except KeyError:
        return None, None

    d: dict = defaultdict(lambda: ['', ''])
    try:
        for key, value in req.items():
            if key[:3] == 'cmd':
                d[int(key[3:])][0] = value
            elif key[:5] == 'value':
                d[int(key[5:])][1] = value
    except:
        return fname, None

    return fname, [i[1] for i in sorted(d.items())]


def check_queries(req_list: List[str]) -> Optional[int]:
    """
    This one checks that the list of queries is correct (that is, cmds are legal and cmds and values are in pairs)
    :param req_list: a list of queries from the previous function
    :return: 1 if ok, None if not
    """
    for r in req_list:
        if r[0] not in QUERIES or len(r) != 2:
            return None
    return 1


def run_queries(req_list: List[str], data: List[str]) -> List[str]:
    """
    Important: only kwargs when calling a func from defaults because of unique query.
    :param req_list: list of queries
    :param data: data
    :return: data after all permutations (as a list)
    """
    for req in req_list:
        data = QUERIES[req[0]](param=req[1], data=data)
    return data


# here be tests

if __name__ == '__main__':
    if a := get_data('apache_logs.txt'):
        print(a[0])
