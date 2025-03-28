from flask import Flask, request, jsonify
from search import search_index

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'running'}), 200

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    results = search_index(query)
    return jsonify({'results': results}), 200

if __name__ == '__main__':
    app.run(debug=True)
