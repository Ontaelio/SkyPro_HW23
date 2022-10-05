import queries.queries as queries

QUERIES = {
    'filter': queries.filter_query,
    'map': queries.map_query,
    'unique': queries.unique_query,
    'sort': queries.sort_query,
    'limit': queries.limit_query,

    'filter_not': queries.filter_not_query,
    'filter_and': queries.filter_and_query,
    'filter_or': queries.filter_or_query,
}