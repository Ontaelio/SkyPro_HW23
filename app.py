from flask import Flask, request, jsonify

from utils import parse_request, get_data, check_queries, run_queries

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/perform_query', methods=['POST'])
def perform_query():

    fname, req = parse_request(request.get_json())

    if not fname:
        return jsonify('Param file_name not provided'), 400

    if not (data := get_data(fname)):
        return jsonify(f'File {fname} not found'), 404

    if not req:
        return jsonify('Query error'), 400

    if not check_queries(req):
        return jsonify('Syntax error in query'), 400

    try:
        data = run_queries(req, data)
    except:
        return jsonify('Error while processing request; wrong value?'), 400

    return jsonify(data)
